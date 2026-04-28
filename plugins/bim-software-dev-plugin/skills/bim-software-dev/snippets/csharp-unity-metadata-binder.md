# C# Unity Metadata Binder

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;

[Serializable]
public class BimMetadata
{
    public string objectId;
    public string elementId;
    public string ifcGuid;
    public string category;
    public string level;
    public string name;
}

public sealed class BimMetadataTarget : MonoBehaviour
{
    public string objectId;
    public BimMetadata metadata;
}

public sealed class BimMetadataBinder : MonoBehaviour
{
    [SerializeField] private Transform modelRoot;
    [SerializeField] private TextAsset metadataCsv;
    [SerializeField] private TextAsset metadataJson;

    private readonly Dictionary<string, BimMetadata> metadataById = new Dictionary<string, BimMetadata>();

    public IReadOnlyDictionary<string, BimMetadata> MetadataById => metadataById;

    private void Start()
    {
        LoadMetadata();
        BindMetadataToObjects();
    }

    private void LoadMetadata()
    {
        metadataById.Clear();

        // Prefer a production CSV or JSON parser for real projects.
        // This example keeps parsing small and runs once at startup, not in Update.
        IEnumerable<BimMetadata> rows = metadataCsv != null
            ? ParseCsv(metadataCsv.text)
            : ParseJson(metadataJson != null ? metadataJson.text : string.Empty);

        foreach (BimMetadata row in rows)
        {
            if (string.IsNullOrWhiteSpace(row.objectId))
            {
                Debug.LogWarning("Metadata row skipped because objectId is missing.");
                continue;
            }

            if (metadataById.ContainsKey(row.objectId))
            {
                Debug.LogWarning($"Duplicate metadata objectId detected: {row.objectId}");
                continue;
            }

            metadataById.Add(row.objectId, row);
        }
    }

    private void BindMetadataToObjects()
    {
        Transform root = modelRoot != null ? modelRoot : transform;
        BimMetadataTarget[] targets = root.GetComponentsInChildren<BimMetadataTarget>(true);
        var boundIds = new HashSet<string>();

        foreach (BimMetadataTarget target in targets)
        {
            if (string.IsNullOrWhiteSpace(target.objectId))
            {
                target.objectId = target.gameObject.name;
            }

            if (metadataById.TryGetValue(target.objectId, out BimMetadata metadata))
            {
                target.metadata = metadata;
                boundIds.Add(target.objectId);
            }
            else
            {
                Debug.LogWarning($"Geometry without metadata: {target.objectId}");
            }
        }

        foreach (string metadataId in metadataById.Keys.Except(boundIds))
        {
            Debug.LogWarning($"Metadata without geometry: {metadataId}");
        }
    }

    private static IEnumerable<BimMetadata> ParseCsv(string csv)
    {
        if (string.IsNullOrWhiteSpace(csv))
        {
            yield break;
        }

        string[] lines = csv.Split(new[] { "\r\n", "\n" }, StringSplitOptions.RemoveEmptyEntries);
        if (lines.Length < 2)
        {
            yield break;
        }

        string[] headers = lines[0].Split(',');

        for (int i = 1; i < lines.Length; i++)
        {
            string[] cells = lines[i].Split(',');
            yield return new BimMetadata
            {
                objectId = GetCell(headers, cells, "object_id"),
                elementId = GetCell(headers, cells, "element_id"),
                ifcGuid = GetCell(headers, cells, "ifc_guid"),
                category = GetCell(headers, cells, "category"),
                level = GetCell(headers, cells, "level"),
                name = GetCell(headers, cells, "name")
            };
        }
    }

    private static IEnumerable<BimMetadata> ParseJson(string json)
    {
        if (string.IsNullOrWhiteSpace(json))
        {
            return Array.Empty<BimMetadata>();
        }

        BimMetadataList wrapper = JsonUtility.FromJson<BimMetadataList>(json);
        return wrapper?.items ?? Array.Empty<BimMetadata>();
    }

    private static string GetCell(string[] headers, string[] cells, string name)
    {
        int index = Array.FindIndex(headers, h => string.Equals(h.Trim(), name, StringComparison.OrdinalIgnoreCase));
        return index >= 0 && index < cells.Length ? cells[index].Trim() : string.Empty;
    }

    [Serializable]
    private sealed class BimMetadataList
    {
        public BimMetadata[] items;
    }
}
```
