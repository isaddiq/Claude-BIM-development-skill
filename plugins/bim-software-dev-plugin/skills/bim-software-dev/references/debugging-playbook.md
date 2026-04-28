# Debugging Playbook

## Revit Add-In Command Not Appearing

Check the `.addin` manifest path, assembly path, full class name, Revit version, .NET target, blocked DLL status, and Revit journal errors. Confirm the command class implements `IExternalCommand` and is public.

## Revit Parameter Extraction Returns Null

Check whether the parameter is instance or type-level, whether the name is localized, whether the element actually has the parameter, and whether the parameter has a value. Try built-in parameters or shared parameter GUIDs when names are unreliable.

## Revit Unit Values Are Wrong

Confirm Revit internal units, output units, and conversion API version. Check whether the parameter is a length, area, volume, angle, or unitless value. Do not assume `AsDouble()` is already in display units.

## Exported CSV Has Missing IDs

Verify the exporter writes `ElementId` and `UniqueId` for every row. Check skipped elements, type rows, linked model records, null source objects, and CSV escaping. Treat missing IDs as critical validation errors.

## Unity Object Selection Works but Metadata Is Empty

Check whether selected objects have a metadata component. If metadata is stored externally, confirm the selected object's ID matches the dictionary key. Inspect importer-renamed GameObjects and duplicate names.

## Unity Metadata Binding Fails

Check CSV or JSON parsing, ID normalization, object hierarchy search, timing of binding relative to model import, duplicate IDs, and missing object IDs. Emit a validation report with geometry without metadata and metadata without geometry.

## Duplicate GameObject Names

Do not bind by name unless names are validated as unique. Add a dedicated ID component, parse a stable ID segment, or create a mapping file. Report every duplicate name and the affected hierarchy paths.

## IFC Extraction Errors

Check IFC schema version, invalid entities, missing property sets, unsupported geometry, broken references, and IfcOpenShell version compatibility. Try extracting metadata separately from geometry to isolate the failure.

## Wrong Coordinates

Check local vs world coordinates, project base point, survey point, true north, project north, georeferencing, linked model transforms, axis convention, and origin shifting.

## Wrong Scale

Check source units, IFC units, Revit feet, Unity meters, import scale factor, glTF units, FBX settings, and any custom conversion code.

## Web Viewer Loads Slowly

Check geometry size, texture size, metadata payload size, network transfer, compression, spatial indexing, progressive loading, and whether all properties are loaded before first render.

## Database Records Do Not Match Objects

Check mapping keys, source file scope, model revision, duplicate IDs, missing IDs, import batch IDs, and any transformations that changed runtime IDs.

## Lost Hierarchy

Check whether the exporter preserved spatial structure, type relationships, systems, and parent-child relationships. Mesh optimization or format conversion may flatten hierarchy unless a separate hierarchy file is exported.

## Geometry Exported but Metadata Missing

Check whether the geometry exporter and metadata exporter use the same filters and identifiers. Validate that every exported geometry object has a matching metadata row.

## Metadata Exported but Geometry Missing

Check non-geometric elements, hidden elements, view filters, unsupported categories, zero-volume solids, symbolic elements, and geometry export failures. Separate expected non-geometric records from errors.
