# C# Unity BIM Guide

## Unity C# BIM Architecture

Unity BIM applications should separate imported geometry, BIM metadata, runtime lookup indexes, selection behavior, and UI presentation.

Recommended layers:

- import layer for model assets
- metadata loading layer for CSV or JSON
- binding layer that maps metadata to GameObjects
- runtime index for fast queries
- selection layer
- property panel UI
- validation reporter

## GameObject Metadata Binding

Attach a metadata component to each BIM GameObject, or maintain an external dictionary keyed by a stable object ID. Do not rely on GameObject names as the only data store.

Useful identifiers:

- IFC GlobalId
- Revit UniqueId
- Revit ElementId
- custom export ID
- imported mesh node ID
- runtime ID

## MonoBehaviour Components

Use `MonoBehaviour` for scene behavior:

- metadata binder
- object selector
- property panel controller
- runtime query service
- validation reporter

Avoid parsing full metadata inside `Update`.

## ScriptableObject Use Cases

Use `ScriptableObject` for reusable configuration or cached datasets:

- category color rules
- property display profiles
- model import settings
- validation rules
- query presets

Do not use `ScriptableObject` as the only source of project-specific metadata unless the data lifecycle is clear.

## CSV/JSON Metadata Loading

CSV is simple and useful for tabular exports. JSON is better for nested property sets, quantities, systems, and hierarchy. For large models, consider loading only an index first, then lazy-loading detailed properties.

## Object Selection and Property Panels

Common flow:

1. Raycast from the camera or pointer.
2. Resolve the selected GameObject.
3. Find the attached BIM metadata component or lookup ID.
4. Load detailed metadata if needed.
5. Update a property panel.
6. Highlight the selected element.

## ID Parsing

If IDs are embedded in GameObject names, define a strict naming convention and parse only the ID segment. Validate duplicates and missing IDs immediately after import.

Better options include metadata components, importer user data, or a separate mapping CSV.

## Runtime Metadata Dictionaries

Use dictionaries for fast lookup:

- `Dictionary<string, BimMetadata>` for ID to metadata
- `Dictionary<string, GameObject>` for ID to object
- `Dictionary<string, List<GameObject>>` when duplicates are possible and must be reported

## Performance for Large BIM Models

Large BIM scenes need:

- category filtering
- object pooling for UI rows
- cached property lists
- asynchronous loading when possible
- spatial partitioning
- mesh combining where selection granularity allows it
- GPU instancing for repeated objects
- metadata lazy loading

## LOD, Batching, Instancing, Lazy Loading

Use LOD for distant or complex objects. Batch static geometry by category or material when object-level selection is not required. Use instancing for repeated assets. Keep detailed property payloads out of memory until selected or queried.

## Coordinate Conversion

Unity uses meters and a Y-up coordinate convention. Revit and IFC data may use feet, millimeters, or georeferenced coordinates. Normalize scale, origin, handedness, and up-axis before binding metadata, navigation, robotics, or XR interactions.

## Common Unity BIM Mistakes

- storing all metadata in GameObject names
- parsing CSV in `Update`
- assuming imported object names are unique
- losing IDs during mesh optimization
- binding metadata before imported objects exist
- ignoring unit conversion
- loading every property into UI at startup
- merging meshes without preserving selection IDs
- failing to report metadata without geometry

## Recommended C# File Structure

- `BimMetadata.cs`
- `BimMetadataBinder.cs`
- `BimObjectSelector.cs`
- `BimPropertyPanel.cs`
- `CsvMetadataLoader.cs`
- `JsonMetadataLoader.cs`
- `BimHierarchyBuilder.cs`
- `BimValidationReporter.cs`
- `BimQueryService.cs`
- `BimRuntimeIndex.cs`
