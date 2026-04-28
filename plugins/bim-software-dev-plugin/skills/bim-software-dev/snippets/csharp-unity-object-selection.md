# C# Unity Object Selection

```csharp
using UnityEngine;

public interface IBimPropertyPanel
{
    void Show(BimMetadata metadata);
    void ShowMissingMetadata(GameObject selectedObject);
    void Clear();
}

public sealed class BimObjectSelector : MonoBehaviour
{
    [SerializeField] private Camera sceneCamera;
    [SerializeField] private LayerMask selectableLayers = ~0;
    [SerializeField] private MonoBehaviour propertyPanelBehaviour;

    private IBimPropertyPanel propertyPanel;

    private void Awake()
    {
        if (sceneCamera == null)
        {
            sceneCamera = Camera.main;
        }

        propertyPanel = propertyPanelBehaviour as IBimPropertyPanel;
    }

    private void Update()
    {
        if (!Input.GetMouseButtonDown(0))
        {
            return;
        }

        SelectFromPointer(Input.mousePosition);
    }

    private void SelectFromPointer(Vector3 screenPosition)
    {
        if (sceneCamera == null)
        {
            Debug.LogWarning("BIM object selection failed because no camera is assigned.");
            return;
        }

        Ray ray = sceneCamera.ScreenPointToRay(screenPosition);

        if (!Physics.Raycast(ray, out RaycastHit hit, float.MaxValue, selectableLayers))
        {
            propertyPanel?.Clear();
            return;
        }

        BimMetadataTarget target = hit.collider.GetComponentInParent<BimMetadataTarget>();
        if (target == null || target.metadata == null)
        {
            propertyPanel?.ShowMissingMetadata(hit.collider.gameObject);
            Debug.LogWarning($"Selected object has no BIM metadata: {hit.collider.gameObject.name}");
            return;
        }

        propertyPanel?.Show(target.metadata);
    }
}
```
