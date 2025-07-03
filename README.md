# Azure Function: Excel to Pandas API

This project is an Azure Function App (Python v2) that exposes an HTTP endpoint to accept an Excel file, convert it to a pandas DataFrame, and return the data as JSON.

## Features
- HTTP-triggered Azure Function
- Accepts Excel files via POST as the raw body (not form-data)
- Converts Excel to pandas DataFrame
- Returns DataFrame as JSON

## Prerequisites
- [Azure Functions Core Tools](https://learn.microsoft.com/azure/azure-functions/functions-run-local)
- Python 3.11+
- [Visual Studio Code](https://code.visualstudio.com/) (recommended)
- Azure subscription (for deployment)

## Local Setup
1. **Clone or open this repo in VS Code.**
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Start the function app locally:**
   ```sh
   func start
   ```
4. **Test the function:**
   - Use Postman or curl to POST an Excel file as the raw body with content-type:
     ```
     Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
     ```
     to:
     ```
     http://localhost:7071/api/ExcelToPandas
     ```
   - Do not use form-data. The file must be sent as the request body.

## Example Request (using curl)
```
curl -X POST "http://localhost:7071/api/ExcelToPandas" \
  -H "Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" \
  --data-binary "@yourfile.xlsx"
```

## Example: Testing with the Provided Sample Excel File

A sample Excel file (`sample.xlsx`) is included in this repository. You can use it to test the function immediately after setup.

### Test the Function with the Sample File
```sh
curl -X POST "http://localhost:7071/api/ExcelToPandas" \
  -H "Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" \
  --data-binary "@sample.xlsx"
```

### Example Output
```json
[
  {"Name": "Alice", "Age": 30},
  {"Name": "Bob", "Age": 25}
]
```

## Running and Debugging in Visual Studio Code
1. Open this project folder in VS Code.
2. Make sure you have the Azure Functions and Python extensions installed.
3. Press **F5** or go to **Run > Start Debugging** to start the function app in debug mode.
4. Set breakpoints in `function_app.py` if you want to debug your code.
5. Once running, test the function as described above (using curl or Postman).

## Deployment
- Deploy to Azure using VS Code or Azure CLI:
  ```sh
  func azure functionapp publish <YourFunctionAppName>
  ```

## Notes
- Only `.xlsx` files are supported (uses `openpyxl`).
- The response is a JSON array of records from the Excel file.
- For large files, consider Azure Blob Storage triggers.

## Troubleshooting
- Ensure all dependencies are installed.
- Check logs in the VS Code terminal for errors.

---

**Author:** Vinod Ramasubbu
