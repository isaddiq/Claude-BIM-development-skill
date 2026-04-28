# Validation and Testing

## Element Count Validation

Compare the number of source elements collected with the number of exported records. Report skipped categories, filtered elements, linked model exclusions, and elements that failed extraction.

## Metadata Row Validation

Every exported metadata row should include the required identifiers, category or class, source file, and enough context to trace it back to the source model.

## ID Matching Validation

Check that geometry objects, metadata rows, database records, and runtime objects can be joined by a defined key. Report unmatched records in both directions.

## Property Preservation Validation

Validate required properties by category or class. Check that expected fields survive export, transformation, storage, and runtime loading.

## Geometry Presence Validation

Report elements with metadata but no geometry and geometry objects with no metadata. Some elements are intentionally non-geometric, so separate expected exceptions from errors.

## Duplicate ID Tests

Test duplicate identifiers in source exports, combined models, linked models, repeated object names, and runtime imports. Binding should fail clearly when duplicate IDs make results ambiguous.

## Missing ID Tests

Test rows and objects with missing IDs. The system should report them and avoid silent fallback binding unless a validated fallback strategy exists.

## Unit Tests

Unit test:

- parameter conversion
- ID normalization
- CSV parsing
- JSON parsing
- unit conversion
- mapping validation
- category filtering
- error handling

## Integration Tests

Integration tests should run an end-to-end path from source model or sample export to the target system. Validate counts, IDs, properties, units, and warnings.

## Revit Test Model Strategy

Maintain small Revit test models with known elements:

- walls, doors, floors, rooms, spaces, and equipment
- instance and type parameters
- missing parameters
- linked model sample if supported
- known unit values
- known categories to skip

## Unity Scene Test Strategy

Create Unity test scenes with:

- imported objects with valid IDs
- duplicate object names
- missing metadata
- metadata without geometry
- scale and coordinate checks
- selectable and non-selectable objects

## Golden Sample Models

Use golden sample models and exports to catch regressions. Store expected validation reports with counts and known warnings.

## Regression Tests

Add regression tests for every production bug. Capture the failing source data, expected behavior, and fixed validation report.

## Performance Tests

Measure:

- export time
- parse time
- binding time
- memory use
- frame rate
- database query latency
- viewer load time

## Validation Report Format

A validation report should include:

- project/model name
- source file
- date
- software version
- source element count
- exported geometry count
- exported metadata count
- matched elements
- missing geometry
- missing metadata
- duplicate IDs
- skipped categories
- unit conversion
- coordinate transformation
- warnings
- errors
- pass/fail status
