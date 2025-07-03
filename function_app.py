import azure.functions as func
import datetime
import json
import logging
import pandas as pd
from io import BytesIO
from requests_toolbelt.multipart.decoder import MultipartDecoder

app = func.FunctionApp()

@app.route(route="ExcelToPandas")
def ExcelToPandas(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    content_type = req.headers.get('content-type') or req.headers.get('Content-Type')
    if not content_type or 'multipart/form-data' not in content_type:
        return func.HttpResponse(
            "Content-Type must be multipart/form-data with 'data_file' and 'meta_file' fields.",
            status_code=400
        )
    try:
        body = req.get_body()
        decoder = MultipartDecoder(body, content_type)
        data_bytes = None
        meta_bytes = None
        for part in decoder.parts:
            content_disp = part.headers.get(b'Content-Disposition', b'').decode()
            if 'name="data_file"' in content_disp:
                data_bytes = part.content
            elif 'name="meta_file"' in content_disp:
                meta_bytes = part.content
        if data_bytes is None or meta_bytes is None:
            return func.HttpResponse(
                "Both 'data_file' and 'meta_file' must be provided in form-data.",
                status_code=400
            )
        # Read metadata (assume JSON for this example)
        meta_json = json.loads(meta_bytes.decode('utf-8'))
        # Read the Excel data file
        df = pd.read_excel(BytesIO(data_bytes), engine="openpyxl")
        # Example: apply column mapping from metadata
        if 'columns' in meta_json:
            df = df[meta_json['columns']]
        result = df.to_json(orient="records")
        return func.HttpResponse(result, mimetype="application/json", status_code=200)
    except Exception as e:
        return func.HttpResponse(
            f"Error processing files: {str(e)}",
            status_code=500
        )