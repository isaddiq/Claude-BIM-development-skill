# C# Revit API Guide

## Revit API Foundation

The Revit API is a C#/.NET based API. Most production add-ins are written in C# and compiled against the Revit API assemblies for a specific Revit version.

## IExternalCommand Pattern

Use `IExternalCommand` for commands launched by the user from the Revit UI. This is the default pattern for examples that export metadata, validate a model, inspect selected elements, or run one-off automation.

The command receives `ExternalCommandData`, which provides access to `UIApplication`, `UIDocument`, and `Document`.

## IExternalApplication Pattern

Use `IExternalApplication` when the add-in needs startup or shutdown behavior, ribbon creation, event registration, application-wide services, or lifecycle management. Do not use it for a simple command unless the add-in needs UI registration or persistent state.

## Transactions

Revit requires transactions only when modifying the document. Read-only extraction does not need a transaction. Opening unnecessary transactions can make commands slower and can interfere with user workflows.

Use:

- `Transaction` for normal document modification
- `TransactionGroup` for grouped operations
- `SubTransaction` only for advanced nested workflows

## FilteredElementCollector

Use `FilteredElementCollector` to collect elements efficiently. Prefer category and class filters before expensive LINQ or parameter checks.

Common filters:

- `.OfCategory(BuiltInCategory.OST_Walls)`
- `.OfClass(typeof(FamilyInstance))`
- `.WhereElementIsNotElementType()`
- `.WhereElementIsElementType()`

## Category and Class Filters

Categories describe Revit organization such as walls, doors, rooms, or mechanical equipment. Classes describe API object types such as `FamilyInstance`, `Wall`, `Floor`, `Room`, or `ElementType`.

Use both when needed. Do not assume every element has a category.

## ElementId vs UniqueId vs IFC GUID

- `ElementId` is an integer-like Revit identifier. It is useful within one model but can change across some workflows.
- `UniqueId` is a more persistent Revit identifier and should usually be exported.
- IFC GUID is useful for IFC exchange, but it may not exist for every element unless exported or stored in a parameter.

For robust mapping, export both `ElementId` and `UniqueId`, and include IFC GUID when available.

## Parameter Reading

Parameters may be instance parameters, type parameters, built-in parameters, shared parameters, or project parameters. They may be missing or have no value.

Read parameters defensively:

- check for `null`
- check `HasValue`
- handle `StorageType`
- use `AsValueString()` where display formatting matters
- convert internal values explicitly where numeric accuracy matters

## StorageType Handling

Handle all common storage types:

- `StorageType.String` with `AsString()`
- `StorageType.Integer` with `AsInteger()`
- `StorageType.Double` with `AsDouble()` plus unit conversion
- `StorageType.ElementId` with `AsElementId()`

Do not assume all parameters are strings.

## Unit Conversion

Revit internal length units are usually feet. Convert values explicitly using the Revit version appropriate unit API. For modern Revit versions, use `UnitUtils` with `UnitTypeId`. For older versions, use `DisplayUnitType`.

Always document the output unit in CSV, JSON, or database schemas.

## Geometry Extraction Limitations

Not every element has extractable geometry. Geometry may be view-dependent, hidden, symbolic, joined, hosted, cut, or unavailable without options. Large geometry extraction can be slow.

Use `Options` deliberately and validate:

- elements with no geometry
- solids with zero volume
- nested instances
- linked model geometry
- view-specific geometry

## Exporting CSV/JSON Metadata

For CSV, flatten stable fields into columns and write flexible parameters as additional columns or a separate property table. Escape delimiters correctly.

For JSON, keep a stable root schema with model metadata, elements, properties, warnings, and validation summary.

## Safe Null Handling

Common nullable values:

- `UIDocument`
- active document
- selected element
- category
- level
- type element
- parameter
- parameter definition
- geometry
- material

Handle missing values explicitly and log skipped records.

## Common Revit API Mistakes

- opening transactions for read-only extraction
- assuming all elements have categories
- assuming all parameters exist
- assuming parameter names are unique
- assuming every element has geometry
- using display values without units
- exporting only `ElementId`
- losing type parameters
- reading only selected elements by accident
- blocking the UI with long exports
- failing to handle linked models

## Recommended C# File Structure

- `BimExternalCommand.cs`
- `RevitElementExtractor.cs`
- `RevitParameterReader.cs`
- `RevitGeometryExporter.cs`
- `BimMetadataExporter.cs`
- `BimMappingValidator.cs`
- `UnitConversionHelper.cs`
- `CsvWriterService.cs`
- `JsonExportService.cs`
- `AddInLogger.cs`
