# C# Revit External Command

```csharp
using System;
using Autodesk.Revit.Attributes;
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;

namespace BimSoftwareDev.Revit
{
    [Transaction(TransactionMode.Manual)]
    public class ExportBimMetadataCommand : IExternalCommand
    {
        public Result Execute(
            ExternalCommandData commandData,
            ref string message,
            ElementSet elements)
        {
            try
            {
                UIDocument uiDocument = commandData.Application.ActiveUIDocument;
                Document document = uiDocument.Document;

                if (document == null)
                {
                    message = "No active Revit document was found.";
                    return Result.Failed;
                }

                // Read-only extraction does not require a transaction.
                // Put BIM metadata extraction, mapping, and export logic here.
                int exportedCount = 0;

                TaskDialog.Show(
                    "BIM Export",
                    $"BIM metadata export completed. Exported elements: {exportedCount}");

                return Result.Succeeded;
            }
            catch (Exception ex)
            {
                message = ex.Message;
                TaskDialog.Show("BIM Export Error", ex.ToString());
                return Result.Failed;
            }
        }
    }
}
```
