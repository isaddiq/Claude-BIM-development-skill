# C# Revit Parameter Extraction

```csharp
using System.Collections.Generic;
using System.Globalization;
using Autodesk.Revit.DB;

namespace BimSoftwareDev.Revit
{
    public static class RevitParameterReader
    {
        public static Dictionary<string, string> ReadElementMetadata(Element element)
        {
            var values = new Dictionary<string, string>();

            if (element == null)
            {
                return values;
            }

            values["ElementId"] = element.Id.IntegerValue.ToString(CultureInfo.InvariantCulture);
            values["UniqueId"] = element.UniqueId ?? string.Empty;
            values["Name"] = element.Name ?? string.Empty;
            values["Category"] = element.Category?.Name ?? string.Empty;

            foreach (Parameter parameter in element.Parameters)
            {
                if (parameter?.Definition == null)
                {
                    continue;
                }

                string parameterName = parameter.Definition.Name;
                values[parameterName] = ReadParameterValue(parameter);
            }

            return values;
        }

        private static string ReadParameterValue(Parameter parameter)
        {
            if (parameter == null || !parameter.HasValue)
            {
                return string.Empty;
            }

            switch (parameter.StorageType)
            {
                case StorageType.String:
                    return parameter.AsString() ?? string.Empty;

                case StorageType.Integer:
                    return parameter.AsInteger().ToString(CultureInfo.InvariantCulture);

                case StorageType.Double:
                    string displayValue = parameter.AsValueString();
                    if (!string.IsNullOrWhiteSpace(displayValue))
                    {
                        return displayValue;
                    }

                    return parameter.AsDouble().ToString(CultureInfo.InvariantCulture);

                case StorageType.ElementId:
                    ElementId id = parameter.AsElementId();
                    return id == ElementId.InvalidElementId
                        ? string.Empty
                        : id.IntegerValue.ToString(CultureInfo.InvariantCulture);

                default:
                    return string.Empty;
            }
        }
    }
}
```
