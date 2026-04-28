# BIM Software Dev Plugin

This Claude Code plugin provides a BIM software development skill for designing, coding, debugging, reviewing, and extending BIM-related software.

The plugin is intended for Revit API add-ins, Unity BIM tools, IFC/OpenBIM workflows, BIM data pipelines, XR viewers, web BIM services, graph databases, digital twins, AI/ML datasets, robotics integrations, model checking, quantity takeoff, and facility management integrations.

## Skill Provided

- `bim-software-dev`

Example command:

```text
/bim-software-dev-plugin:bim-software-dev create a C# Revit add-in that exports BIM metadata to CSV
```

Some Claude Code versions may expose skill shortcuts differently. If the command name differs, check `/plugin` and `/skills`.

## Supported Languages

- C# for Revit API, Unity, XR, .NET desktop tools, and BIM utilities
- Python for IfcOpenShell, automation, validation, conversion, and data engineering
- TypeScript and JavaScript for web viewers, APIs, dashboards, and BIM data services
- SQL for relational BIM databases
- Cypher for graph database queries
- C++ for geometry processing, native extensions, plugins, and performance-sensitive logic

The skill gives strong C# support for Revit and Unity workflows, including Revit add-ins, Revit metadata extraction, Unity runtime metadata binding, object selection, validation reporting, and large model performance strategies.

## Example Prompts

```text
/bim-software-dev-plugin:bim-software-dev create a C# Revit add-in that exports ElementId, UniqueId, category, family, type, level, and parameters to CSV
```

```text
/bim-software-dev-plugin:bim-software-dev create Unity C# scripts to bind BIM metadata from CSV to imported GameObjects and show properties on object selection
```

```text
/bim-software-dev-plugin:bim-software-dev debug why my Revit-exported OBJ objects appear in Unity but metadata does not bind
```

```text
/bim-software-dev-plugin:bim-software-dev design an IFC to graph database pipeline for BIM semantic queries
```

```text
/bim-software-dev-plugin:bim-software-dev create a BIM-to-robotics semantic scene graph pipeline
```
