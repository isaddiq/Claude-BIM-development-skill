# TypeScript BIM API Service

```typescript
export interface BimElementMetadata {
  elementId: string;
  sourceFile?: string;
  ifcGuid?: string;
  revitUniqueId?: string;
  objectName?: string;
  category?: string;
  level?: string;
  properties: Record<string, string | number | boolean | null>;
}

export interface BimQuery {
  elementId?: string;
  category?: string;
}

export class BimMetadataRepository {
  private readonly elementsById = new Map<string, BimElementMetadata>();

  upsert(element: BimElementMetadata): void {
    this.elementsById.set(element.elementId, element);
  }

  getByElementId(elementId: string): BimElementMetadata | undefined {
    return this.elementsById.get(elementId);
  }

  filterByCategory(category: string): BimElementMetadata[] {
    return [...this.elementsById.values()].filter(
      (element) => element.category === category,
    );
  }
}

// REST-like handlers. Wire these to Express, Fastify, Next.js, or another server.
export function getElementHandler(repository: BimMetadataRepository, elementId: string) {
  const element = repository.getByElementId(elementId);

  if (!element) {
    return { status: 404, body: { error: "BIM element not found", elementId } };
  }

  return { status: 200, body: element };
}

export function filterElementsHandler(repository: BimMetadataRepository, query: BimQuery) {
  if (query.elementId) {
    const element = repository.getByElementId(query.elementId);
    return { status: 200, body: element ? [element] : [] };
  }

  if (query.category) {
    return { status: 200, body: repository.filterByCategory(query.category) };
  }

  return { status: 400, body: { error: "Provide elementId or category" } };
}

// Keep metadata in API/database storage and geometry in separate model files.
// Link both through stable BIM identifiers.
```
