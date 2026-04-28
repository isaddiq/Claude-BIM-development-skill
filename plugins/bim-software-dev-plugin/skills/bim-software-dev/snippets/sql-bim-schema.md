# SQL BIM Schema

```sql
CREATE TABLE bim_models (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    source_file TEXT NOT NULL,
    source_tool TEXT,
    model_revision TEXT,
    created_at TEXT NOT NULL
);

CREATE TABLE bim_elements (
    id INTEGER PRIMARY KEY,
    model_id INTEGER NOT NULL,
    element_id TEXT NOT NULL,
    ifc_guid TEXT,
    revit_unique_id TEXT,
    object_name TEXT,
    category TEXT,
    element_type TEXT,
    level_name TEXT,
    family_name TEXT,
    type_name TEXT,
    FOREIGN KEY (model_id) REFERENCES bim_models(id),
    UNIQUE (model_id, element_id)
);

CREATE TABLE bim_properties (
    id INTEGER PRIMARY KEY,
    element_id INTEGER NOT NULL,
    property_set TEXT,
    property_name TEXT NOT NULL,
    property_value TEXT,
    value_type TEXT,
    unit TEXT,
    FOREIGN KEY (element_id) REFERENCES bim_elements(id)
);

CREATE TABLE bim_id_mappings (
    id INTEGER PRIMARY KEY,
    model_id INTEGER NOT NULL,
    source_file TEXT,
    source_tool TEXT,
    source_id TEXT,
    ifc_guid TEXT,
    revit_unique_id TEXT,
    runtime_id TEXT,
    object_name TEXT,
    category TEXT,
    level_name TEXT,
    status TEXT NOT NULL,
    FOREIGN KEY (model_id) REFERENCES bim_models(id)
);

CREATE TABLE validation_reports (
    id INTEGER PRIMARY KEY,
    model_id INTEGER NOT NULL,
    report_path TEXT,
    source_element_count INTEGER NOT NULL DEFAULT 0,
    exported_geometry_count INTEGER NOT NULL DEFAULT 0,
    exported_metadata_count INTEGER NOT NULL DEFAULT 0,
    matched_elements INTEGER NOT NULL DEFAULT 0,
    missing_geometry_count INTEGER NOT NULL DEFAULT 0,
    missing_metadata_count INTEGER NOT NULL DEFAULT 0,
    duplicate_id_count INTEGER NOT NULL DEFAULT 0,
    warning_count INTEGER NOT NULL DEFAULT 0,
    error_count INTEGER NOT NULL DEFAULT 0,
    pass_fail_status TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (model_id) REFERENCES bim_models(id)
);
```
