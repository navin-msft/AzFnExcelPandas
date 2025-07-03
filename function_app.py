import azure.functions as func
import datetime
import json
import logging
import pandas as pd
from io import BytesIO

app = func.FunctionApp()

@app.route(route="ExcelToPandas")
def ExcelToPandas(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Expect the Excel file as the raw body
    content_type = req.headers.get('content-type') or req.headers.get('Content-Type')
    if not content_type or 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' not in content_type:
        return func.HttpResponse(
            "Content-Type must be 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' and the body must be the Excel file.",
            status_code=400
        )
    try:
        file_bytes = req.get_body()
        df = pd.read_excel(BytesIO(file_bytes), engine="openpyxl")
        result = df.to_json(orient="records")
        return func.HttpResponse(result, mimetype="application/json", status_code=200)
    except Exception as e:
        return func.HttpResponse(
            f"Error processing Excel file: {str(e)}",
            status_code=500
        )