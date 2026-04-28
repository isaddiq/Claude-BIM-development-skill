# BIM Software Principles

## BIM Is Data Plus Geometry

BIM software should treat a model as structured project data linked to geometry. Geometry is only one view of the model. The usable BIM value comes from identifiers, classifications, property sets, quantities, systems, spatial hierarchy, phases, and provenance.

## Source of Truth Principle

Decide which system owns each class of information:

- Revit, Archicad, Tekla, or another authoring tool may own design intent.
- IFC may own exchange state.
- A database may own normalized analytics data.
- A digital twin may own operational state.
- Unity, Unreal, or a web viewer should usually consume and display data rather than become the permanent source of authoritative BIM metadata.

Avoid silent edits in secondary systems unless there is a defined synchronization and conflict resolution strategy.

## Model Provenance

Every exported record should preserve where it came from:

- source file
- source tool and version
- export date
- model revision
- element identifier
- export pipeline version
- transformation notes

Provenance makes debugging, validation, audit, and round-trip workflows possible.

## Geometry and Metadata Separation

Store geometry and metadata separately when practical, then link them through stable identifiers. Geometry formats such as OBJ, glTF, FBX, or mesh assets rarely preserve complete BIM semantics by themselves. Metadata should be stored in CSV, JSON, SQL, graph databases, or API payloads and bound back to geometry by ID.

## Direct API vs File Exchange

Use direct APIs when:

- you need native identifiers and parameters
- you need high fidelity extraction
- you need controlled exports
- you are building add-ins or automation inside the authoring tool
- you need reliable unit and category handling

Use file exchange when:

- the source system is unavailable at runtime
- the workflow must be vendor-neutral
- the data must cross organization or software boundaries
- you need openBIM compatibility
- the model is already exchanged as IFC, glTF, OBJ, or another format

## OpenBIM vs Proprietary API Tradeoffs

OpenBIM formats such as IFC improve portability, interoperability, and long-term accessibility. Proprietary APIs such as Revit API expose richer native behavior, parameters, category semantics, and editing operations.

OpenBIM workflows can lose native authoring details. Proprietary workflows can lock the solution to a specific toolchain. Choose based on the business requirement, not only the file format.

## Round-Trip Limitations

Round-tripping is rarely lossless. Geometry, parameters, constraints, hosted relationships, family behavior, materials, analytical data, and classifications may change or disappear. Any round-trip workflow needs an explicit diff and validation process.

## Validation-First Development

Every BIM transformation should produce a validation report. At minimum, compare source element counts, exported geometry counts, metadata row counts, ID matches, duplicate IDs, missing IDs, skipped categories, unit conversion, coordinate transforms, warnings, and errors.

## Performance-Aware BIM Software Design

Large BIM models require deliberate performance choices:

- filter categories and properties before export
- avoid loading all metadata into UI controls
- use batching, instancing, and LOD for visualization
- stream or page data where possible
- index IDs and spatial regions
- cache parsed metadata
- avoid per-frame parsing or database calls

## Extensible Schema Design

Use schemas that can grow as project requirements change. Keep core fields stable, then store flexible property sets in child tables, JSON objects, or graph properties. Include version fields so exported data can be migrated safely.

## Object Names Are Weak Metadata Stores

GameObject names, mesh names, file names, and layer names are useful hints but poor metadata stores. They are often duplicated, truncated, edited by artists, changed by importers, or stripped during optimization. Use names only as fallback IDs unless the pipeline guarantees uniqueness and immutability.
