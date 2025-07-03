# Azure Function: Excel to Pandas API with Metadata

This project is an Azure Function App (Python v2) that exposes an HTTP endpoint to accept an Excel data file and a metadata file, process the data according to the metadata, and return the result as JSON.

## Features
- HTTP-triggered Azure Function
- Accepts two files via POST (`multipart/form-data`):
  - `data_file`: Excel file (`.xlsx`)
  - `meta_file`: JSON file (e.g., column selection)
- Uses metadata to interpret/process the data file (e.g., select columns)
- Returns processed data as JSON

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

## Usage: Upload Data and Metadata Files
You must send both a data file (Excel) and a metadata file (JSON) in a single request using `multipart/form-data`.

### Example Request (using curl)
```sh
curl -X POST "http://localhost:7071/api/ExcelToPandas" \
  -H "Content-Type: multipart/form-data" \
  -F "data_file=@sample_data.xlsx" \
  -F "meta_file=@sample_meta.json"
```

### Example Request (using Postman)
- Set method to POST and URL to `http://localhost:7071/api/ExcelToPandas`
- In the Body tab, select `form-data`
- Add two fields:
  - `data_file`: select your Excel file (e.g., `sample_data.xlsx`)
  - `meta_file`: select your JSON file (e.g., `sample_meta.json`)

## Sample Files
- `sample_data.xlsx`: Example Excel file with columns `Name`, `Age`, `City`
- `sample_meta.json`: Example metadata file:
  ```json
  {
    "columns": ["Name", "City"]
  }
  ```

## Example Output
```json
[
  {"Name": "Alice", "City": "NY"},
  {"Name": "Bob", "City": "LA"}
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
- Only `.xlsx` files are supported for data (uses `openpyxl`).
- The metadata file must be valid JSON. You can extend the metadata logic as needed.
- The response is a JSON array of records from the Excel file, processed according to the metadata.
- For large files, consider Azure Blob Storage triggers.

## Troubleshooting
- Ensure all dependencies are installed.
- Check logs in the VS Code terminal for errors.

---

**Author:** Vinod Ramasubbu
