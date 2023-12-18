from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from io import StringIO
from models.graph_model import graph_request_body
from service import graph_service
import pandas as pd
import uuid, os

router = APIRouter()

@router.get("/ping")
async def graph_ping():
    status = 200
    content={
        "is successful": "true"
    }
    return JSONResponse(status_code=status, content=content)

@router.post("/get_graph")
async def get_graph(data: graph_request_body.Graph_Request_Body):
    status = 200
    filePath = data.filePath
    fileType = os.path.splitext(filePath)[1]
    if fileType == ".csv":
        df = graph_service.convert_csv_to_dataframe(filePath)
    elif fileType == ".xls" or fileType == ".xlsx":
        df = graph_service.convert_xls_to_dataframe(filePath)
    else:
        df = pd.DataFrame
    graph = graph_service.get_graph(df, data.src, data.dest)
    response = {
        "data": {
            "graph": graph
        }
    }
    return JSONResponse(status_code=status, content=response)

@router.post("/post_data")
async def post_data(file: UploadFile = File(...)):
    status=200
    unique_id = uuid.uuid4()
    fileName = file.filename
    fileType = os.path.splitext(fileName)[1]
    uploaded_file_path=f"user_data/uploaded_data/uploaded_{unique_id}{fileType}"
    with open(uploaded_file_path, "wb") as buffer:
        buffer.write(file.file.read())
    fileHeaders = graph_service.getHeaders(uploaded_file_path, fileType)
    response = {
        "data": {
            "filePath": uploaded_file_path,
            "fileHeaders": fileHeaders
        }
    }
    return JSONResponse(status_code=status, content=response)