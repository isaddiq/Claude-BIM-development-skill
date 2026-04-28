---
name: bim-software-dev
description: BIM software development and BIM data engineering skill. Use when designing, coding, debugging, reviewing, or extending software related to BIM, IFC, OpenBIM, Revit API, Unity, XR, Unreal, Archicad, IfcOpenShell, Speckle, web BIM viewers, BIM databases, graph databases, digital twins, AI/ML datasets, robotics, SLAM, model checking, quantity takeoff, facility management, semantic validation, construction data pipelines, or BIM integration with other technologies. Strongly apply this skill for C# Revit add-ins, C# Unity BIM applications, BIM metadata binding, BIM geometry processing, BIM API development, and BIM data validation. Do not use for general architectural writing, non-BIM 3D graphics, generic Unity games, or ordinary software tasks without BIM data.
argument-hint: "[BIM programming task, bug, feature, integration, API, Revit add-in, Unity BIM tool, IFC pipeline, or data workflow]"
---

# BIM Software Development Skill

Use this skill for software engineering tasks related to BIM, BIM data, BIM automation, BIM visualization, BIM analytics, and BIM integration with other technologies.

This skill is broader than interoperability. It supports complete BIM-related development, including extraction, transformation, validation, storage, visualization, automation, APIs, AI/ML preparation, XR interaction, digital twins, robotics, model checking, and facility management integration.

## Priority language support

Give strongest priority to C# when the task involves:

- Revit API
- Revit add-ins
- Autodesk add-in development
- Unity
- XR or mixed reality applications
- BIM object selection in Unity
- runtime metadata binding
- .NET desktop tools
- C# BIM utilities

Also support:

- Python for IfcOpenShell, automation, validation, conversion, and data engineering
- TypeScript and JavaScript for web viewers, APIs, dashboards, and BIM data services
- SQL for BIM databases
- Cypher for graph databases
- C++ for geometry, plugins, native extensions, and performance-sensitive logic
- JSON, CSV, XML, IFC, IDS, BCF, glTF, OBJ, FBX, USD, and other BIM-related formats

## Core mindset

Treat BIM as structured project data plus geometry, not only 3D objects.

For every BIM development task, consider:

1. Source BIM environment
2. Target software or platform
3. Programming language
4. Data format
5. Geometry strategy
6. Metadata strategy
7. Identifier strategy
8. Unit handling
9. Coordinate system handling
10. Object hierarchy
11. Validation method
12. Performance constraints
13. Error handling
14. Testing strategy
15. Data loss and limitations

## First response behavior

When the user asks for BIM software development help:

1. Identify the likely source:
   - Revit
   - IFC
   - Archicad
   - Tekla
   - Rhino/Grasshopper
   - Speckle
   - CSV/JSON/SQL BIM data
   - Unity BIM scene
   - web BIM model
   - unknown source

2. Identify the likely target:
   - Revit add-in
   - Unity/XR
   - Unreal
   - web viewer
   - database
   - graph database
   - API service
   - AI/ML pipeline
   - robotics/SLAM
   - digital twin
   - facility management system
   - model checking tool
   - quantity takeoff tool

3. Choose the most appropriate programming stack:
   - C# for Revit and Unity
   - Python for IFC and automation
   - TypeScript for web/API
   - SQL/Cypher for storage and graph queries
   - C++ only when native performance is required

4. If enough information exists, proceed with reasonable assumptions.
5. If one missing detail blocks implementation, ask only that question.
6. Prefer working architecture, code, validation, and tests over abstract explanation.

## Non-negotiable BIM software rules

### Preserve identifiers

Never design a BIM tool without defining the joining key between geometry, metadata, database records, and runtime objects.

Possible identifiers:

- IFC GlobalId
- Revit ElementId
- Revit UniqueId
- Archicad Element ID
- Speckle object ID
- custom persistent ID
- database primary key
- runtime object ID

When multiple identifiers exist, create a mapping table.

### Preserve metadata

BIM elements must remain queryable after export, conversion, database storage, or runtime loading.

Preserve, when relevant:

- element class
- element name
- element type
- family/type information
- level/storey
- space/zone
- material
- property sets
- classifications
- quantities
- systems
- phase/status
- spatial location
- source file
- source identifier

### Validate every transformation

Any BIM software pipeline should report:

- source element count
- exported geometry count
- exported metadata count
- matched object count
- missing IDs
- duplicate IDs
- geometry without metadata
- metadata without geometry
- skipped categories/classes
- unit conversion
- coordinate transformation
- hierarchy reconstruction status
- warnings
- errors

### Handle units and coordinates

Always check:

- millimeters vs meters vs feet
- Revit internal feet
- IFC project units
- Unity meters
- local coordinates vs world coordinates
- project north vs true north
- georeferenced vs local models
- right-handed vs left-handed coordinates
- Unity Y-up convention
- GIS coordinate reference systems when relevant

### Design for large BIM models

For Unity, XR, web, robotics, or digital twins, consider:

- LOD
- instancing
- batching
- mesh simplification
- property filtering
- lazy metadata loading
- spatial indexing
- database-backed metadata
- streaming
- caching
- compressed formats
- progressive loading

## C# Revit API rules

When writing Revit API code:

1. Use IExternalCommand for command examples unless another pattern is requested.
2. Use IExternalApplication only when startup, ribbon, lifecycle, or application-level behavior is needed.
3. Use transactions only when modifying the Revit document.
4. Do not open unnecessary transactions for read-only extraction.
5. Prefer FilteredElementCollector with category/class filters.
6. Extract both ElementId and UniqueId.
7. Extract IFC GUID only when it exists or can be retrieved reliably.
8. Extract parameters safely with null checks.
9. Handle StorageType correctly:
   - String
   - Integer
   - Double
   - ElementId
10. Remember Revit internal units are usually feet.
11. Convert units explicitly.
12. Avoid assuming every element has geometry.
13. Avoid assuming every element has a category.
14. Avoid assuming every parameter exists.
15. Log skipped elements.
16. Keep add-in logic modular:
   - command layer
   - extraction layer
   - mapping layer
   - export layer
   - validation layer

Preferred Revit C# modules:

- BimExternalCommand.cs
- RevitElementExtractor.cs
- RevitParameterReader.cs
- RevitGeometryExporter.cs
- BimMetadataExporter.cs
- BimMappingValidator.cs
- UnitConversionHelper.cs
- CsvWriterService.cs
- JsonExportService.cs

## C# Unity BIM rules

When writing Unity BIM code:

1. Use C# MonoBehaviour examples unless another architecture is requested.
2. Do not store full metadata only in GameObject names.
3. Use GameObject names only as lightweight IDs if unavoidable.
4. Prefer a metadata component attached to BIM objects.
5. Support lazy loading for large metadata.
6. Support object selection and metadata display.
7. Keep metadata binding separate from UI logic.
8. Use dictionaries for ID-to-metadata lookup.
9. Validate unbound geometry objects.
10. Validate metadata rows that do not match objects.
11. Handle duplicate object names or duplicate IDs.
12. Avoid heavy parsing during every frame.
13. Use caching.
14. Consider Addressables, asset bundles, or streaming for large models.

Preferred Unity C# modules:

- BimMetadata.cs
- BimMetadataBinder.cs
- BimObjectSelector.cs
- BimPropertyPanel.cs
- CsvMetadataLoader.cs
- JsonMetadataLoader.cs
- BimHierarchyBuilder.cs
- BimValidationReporter.cs
- BimQueryService.cs
- BimRuntimeIndex.cs

## Development output formats

### For new BIM software features

Respond with:

1. Recommended architecture
2. Technology stack
3. Data flow
4. Identifier strategy
5. File/module structure
6. Implementation code
7. Validation checks
8. Test cases
9. Known limitations
10. Next improvement path

### For C# Revit add-ins

Respond with:

1. Add-in goal
2. Revit API approach
3. Required classes
4. Data extraction strategy
5. Identifier strategy
6. Unit conversion strategy
7. C# code
8. Add-in manifest notes if needed
9. Validation checks
10. Testing inside Revit

### For C# Unity BIM applications

Respond with:

1. Unity scene architecture
2. Data loading strategy
3. Metadata binding strategy
4. GameObject ID strategy
5. C# scripts
6. UI interaction logic
7. Performance strategy
8. Validation checks
9. Testing method

### For debugging

Respond with:

1. Suspected failure layer
2. Most likely cause
3. Minimal fix
4. Safer long-term fix
5. Code patch
6. Validation test
7. Regression prevention

Failure layers:

- Revit extraction
- IFC extraction
- geometry export
- metadata export
- identifier mapping
- file parsing
- database schema
- API communication
- unit conversion
- coordinate transform
- runtime binding
- Unity object selection
- query logic
- visualization
- performance

### For code review

Check:

1. BIM identifier preservation
2. metadata completeness
3. unit handling
4. coordinate handling
5. null safety
6. error handling
7. performance risks
8. hardcoded assumptions
9. data loss
10. test coverage
11. extensibility

### For AI/ML with BIM

Require:

1. clear learning target
2. data schema
3. feature extraction method
4. label source
5. BIM provenance
6. train/validation/test split
7. leakage prevention
8. evaluation metric
9. integration back into BIM, XR, or digital twin

Do not recommend training directly on raw BIM files without a structured intermediate dataset.

### For BIM-to-robotics

Separate:

1. BIM semantic model
2. robot perception model
3. coordinate registration
4. navigation/task planning
5. sensor feedback
6. BIM/digital twin update

Never assume BIM geometry is directly usable for robot navigation.

## Additional references

Load these files when needed:

- references/bim-software-principles.md
- references/csharp-revit-api-guide.md
- references/csharp-unity-bim-guide.md
- references/data-and-identifier-strategy.md
- references/architecture-patterns.md
- references/language-specific-patterns.md
- references/validation-and-testing.md
- references/debugging-playbook.md

Use these templates when creating specifications:

- templates/feature-spec.md
- templates/revit-addin-spec.md
- templates/unity-bim-viewer-spec.md
- templates/bim-data-pipeline-spec.md
- templates/api-integration-spec.md
- templates/validation-report-template.md

Use snippets when writing code examples:

- snippets/csharp-revit-external-command.md
- snippets/csharp-revit-parameter-extraction.md
- snippets/csharp-unity-metadata-binder.md
- snippets/csharp-unity-object-selection.md
- snippets/python-ifcopenshell-extraction.md
- snippets/typescript-bim-api-service.md
- snippets/sql-bim-schema.md

Use this helper script when validating mapping CSV files:

- scripts/validate_bim_mapping.py

Now create the supporting files.
