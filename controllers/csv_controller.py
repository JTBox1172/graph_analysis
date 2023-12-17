from fastapi import APIRouter, UploadFile, File, BackgroundTasks
from fastapi.responses import FileResponse, JSONResponse
from service import clean_csv
from models import gama_retrieval_body
import pandas as pd
import json
import os
import uuid

router = APIRouter()

@router.post("/gama/upload", tags=["csv"])
async def csv_Endpoint(file: UploadFile = File(...)):
    status=200
    unique_id = uuid.uuid4()
    uploaded_file_path=f"user_data/uploaded_data/uploaded_{unique_id}.csv"
    clean_file_path=f"user_data/return_data/cleaned_{unique_id}.csv"
    file_paths = {
        "uploaded_file_path": uploaded_file_path,
        "clean_file_path": clean_file_path
        }
    with open(uploaded_file_path, "wb") as buffer:
        buffer.write(file.file.read())
    data = clean_csv.clean_csv_gama(file_paths)
    response = {
        "data": {
            "filePath": clean_file_path,
            "fileName": f"cleaned_{file.filename}",
            "data": data
        }
    }
    try:
        os.remove(uploaded_file_path)
    except Exception as e:
        print(e)
    return JSONResponse(status_code=status, content=response)
    

@router.get("/test", tags=["csv"])
async def api_test_endpoint():
    status = 200
    content={
        "cleaned": "True",
        "Filename": 'would be a filename'
    }
    return JSONResponse(status_code=status, content=content)

@router.post("/gama/retrieve", tags=["csv"])
async def getUploadedData(body: gama_retrieval_body.retrievalBody, background_tasks: BackgroundTasks):
    status = 200
    response = FileResponse(status_code=status, path=body.filePath, filename=body.fileName, headers={"metadata":"metadata"})
    background_tasks.add_task(removeFile, body.filePath)
    return response

def removeFile(path):
    print(f"removing {path}")
    try:
        os.remove(path)
    except Exception as e:
        print(e)
