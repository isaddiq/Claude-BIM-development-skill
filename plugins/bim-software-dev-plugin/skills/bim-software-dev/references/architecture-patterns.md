# BIM Architecture Patterns

## Revit Add-In Exporting BIM Metadata

Use a Revit `IExternalCommand` that collects elements with `FilteredElementCollector`, extracts `ElementId`, `UniqueId`, category, type, level, parameters, and optional IFC GUID, then writes CSV or JSON plus a validation report.

Core modules:

- command layer
- element extractor
- parameter reader
- metadata exporter
- mapping validator
- logger

## Revit to Unity

Export geometry to FBX, OBJ, glTF, or a Unity-friendly format. Export metadata separately to CSV or JSON. Preserve a shared object ID in both geometry object names or importer metadata and the metadata file. Bind at Unity startup and report unmatched objects.

## Revit to Database

Use a Revit add-in or automation workflow to extract metadata into CSV, JSON, or direct API payloads. Normalize stable element fields into relational tables and store flexible parameters in child rows or JSON columns. Include model revision and source identifiers.

## IFC to Database

Use IfcOpenShell or a BIM ETL service to parse IFC entities, property sets, quantities, spatial structure, and relationships. Store entities and properties with IFC `GlobalId` as the primary source identifier. Validate entity counts and property extraction coverage.

## IFC to Unity/XR

Convert IFC geometry to glTF, FBX, or Unity mesh assets. Extract metadata to JSON or a database. Use IFC `GlobalId` as the binding key. Optimize geometry with LOD, batching, instancing, and spatial partitioning.

## IFC to Web Viewer

Use a web viewer format such as glTF, fragments, or a specialized IFC viewer pipeline. Store metadata separately in JSON or API-backed storage. Provide query endpoints by `GlobalId`, category, type, level, and property.

## Archicad to Unity

Use IFC, Datasmith, FBX, or an Archicad API export depending on fidelity requirements. Preserve Archicad IDs and IFC `GlobalId` where possible. Validate object names because importer pipelines may rename nodes.

## Speckle to Web or Unity

Use Speckle object IDs and source application IDs. Pull data through Speckle APIs, normalize metadata, and map Speckle objects to runtime objects. Preserve stream, branch, commit, and object provenance.

## BIM to Graph Database

Represent elements, spaces, levels, systems, materials, classifications, and relationships as nodes and edges. Use IFC `GlobalId`, Revit `UniqueId`, or another source ID as a stable property. Use graph queries for containment, adjacency, system connectivity, and semantic validation.

## BIM to AI/ML Dataset

Extract a structured intermediate dataset. Define features, labels, provenance, train/validation/test split, and leakage controls. Do not train directly on raw BIM files without normalizing entities and documenting assumptions.

## BIM to Digital Twin

Separate static BIM data from live operational data. Map BIM elements to sensors, assets, rooms, equipment, and maintenance records. Include source identifiers, time-series IDs, update frequency, synchronization rules, and conflict handling.

## BIM to Robotics/SLAM

Separate BIM semantics from robot perception. Convert relevant spaces, obstacles, and assets into a robot-usable scene graph or map. Register BIM coordinates to robot coordinates and validate with sensor feedback. Do not assume BIM geometry is navigation-ready.

## BIM Rule Checker

Parse model data into a queryable representation, run rules against categories, properties, spaces, dimensions, clearances, classifications, or relationships, and output pass/fail results with element IDs and human-readable explanations.

## BIM Quantity Takeoff Tool

Extract quantities from trusted source properties when available. Compute quantities from geometry only when the assumptions are documented. Preserve units, element IDs, classifications, and calculation method.
