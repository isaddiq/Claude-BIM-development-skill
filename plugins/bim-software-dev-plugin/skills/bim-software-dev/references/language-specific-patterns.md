# Language-Specific BIM Patterns

## C# Revit API

Use C# Revit API when building add-ins, commands, metadata exporters, model checkers, automation inside Revit, or tools that need native Revit data.

Do not use it when the workflow must run without Revit or when openBIM file processing is enough.

## C# Unity

Use C# Unity for BIM visualization, XR, object selection, metadata binding, interactive training, digital twin viewers, and runtime simulation.

Do not use Unity as the authoritative BIM database unless synchronization and persistence are explicitly designed.

## C# .NET Desktop Tools

Use C# .NET desktop tools for Windows BIM utilities, batch processors, validation tools, WPF dashboards, add-in companion apps, and enterprise integrations.

Do not use desktop tools for cloud-first APIs or browser-first workflows unless there is a clear deployment reason.

## Python IfcOpenShell

Use Python with IfcOpenShell for IFC parsing, property extraction, conversion, validation, and ETL workflows.

Do not use it for native Revit editing or workflows that require full Revit API behavior.

## Python Data Processing

Use Python for CSV/JSON processing, validation reports, machine learning dataset preparation, analytics, and quick automation scripts.

Do not use Python scripts as hidden production infrastructure without logging, repeatability, and test coverage.

## TypeScript API Service

Use TypeScript for BIM metadata APIs, web dashboards, validation services, model query endpoints, and typed integrations with frontend clients.

Do not put heavy geometry processing in TypeScript unless the platform and performance profile are proven.

## JavaScript Web Viewer

Use JavaScript for browser-based BIM viewing, UI interaction, metadata panels, filtering, and selection behavior.

Do not rely on browser memory for full metadata payloads from very large models without lazy loading or paging.

## SQL Relational Schema

Use SQL for normalized metadata storage, reporting, joins, validation tables, model revisions, and enterprise integration.

Do not force deeply connected semantic relationships into SQL-only designs when graph traversal is the primary workload.

## Cypher Graph Queries

Use Cypher and graph databases for containment, adjacency, systems, dependencies, semantic validation, route queries, and digital twin relationships.

Do not use graph databases only as a replacement for simple tabular reporting.

## C++ Geometry Processing

Use C++ for native plugins, computational geometry, mesh processing, format conversion, and performance-sensitive operations.

Do not use C++ for ordinary metadata APIs or UI workflows unless native integration is required.
