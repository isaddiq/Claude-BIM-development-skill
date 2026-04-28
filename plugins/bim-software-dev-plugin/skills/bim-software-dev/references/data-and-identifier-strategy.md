# Data and Identifier Strategy

## Common BIM Identifiers

### IFC GlobalId

The IFC `GlobalId` is the preferred identifier for IFC-based exchange. It is portable across IFC workflows when preserved correctly.

### Revit ElementId

Revit `ElementId` is useful inside a specific Revit document and session. Export it for traceability, but avoid using it as the only persistent cross-system key.

### Revit UniqueId

Revit `UniqueId` is usually more stable than `ElementId` and should be exported for Revit-based data pipelines.

### Archicad Element ID

Archicad element IDs can support mapping from Archicad exports or APIs. Validate whether they are unique and stable in the chosen workflow.

### Speckle Object ID

Speckle object IDs are useful when Speckle is the exchange or collaboration layer. Preserve source application IDs alongside Speckle IDs.

### Custom Persistent ID

Use a custom persistent ID when no source identifier is stable enough or when the pipeline merges data from multiple systems. Define how it is generated, stored, and migrated.

### Database ID

Database IDs are useful for internal storage but should not replace source BIM identifiers. Use them as surrogate keys with source IDs stored as unique or indexed fields.

### Runtime ID

Runtime IDs help map imported geometry, GameObjects, viewer nodes, or robotics scene objects. They should be mapped back to source IDs.

## Mapping Table Design

Create a mapping table whenever geometry, metadata, database records, and runtime objects use different identifiers.

Recommended mapping table columns:

- `source_file`
- `source_tool`
- `source_id`
- `ifc_guid`
- `revit_unique_id`
- `runtime_id`
- `object_name`
- `category`
- `level`
- `status`

Additional useful columns:

- `database_id`
- `export_batch_id`
- `model_revision`
- `created_at`
- `updated_at`
- `warning`

## Duplicate ID Detection

Detect duplicates before binding or importing data. Duplicate IDs may indicate repeated object names, bad export settings, linked model conflicts, or ID truncation.

For duplicates:

1. record all conflicting rows
2. block automatic binding when ambiguity affects correctness
3. include source file and category in the report
4. create a deterministic conflict resolution rule only when the business workflow allows it

## Missing ID Handling

Missing IDs are critical for BIM software. Handle them by:

- reporting the row or object
- assigning a temporary runtime ID only for diagnostics
- excluding the object from authoritative sync
- fixing the exporter when possible

Do not silently bind metadata by display name unless the pipeline explicitly validates uniqueness.

## Collision Handling

ID collisions can happen when combining models, linked files, or exports from multiple tools. Use composite keys such as `source_file + source_tool + source_id` or assign a stable project-level ID.

## Minimal Mapping Rules

- Geometry must have an ID.
- Metadata must have an ID.
- Database records must preserve the source ID.
- Runtime objects must expose or store the ID.
- Validation must report unmatched records in both directions.
