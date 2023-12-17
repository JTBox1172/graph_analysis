from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/upload")
async def excel_enpoint(file: UploadFile = File(...)):
    status = 200
    with open(f"uploaded_{file.filename}", "wb") as buffer:
        buffer.write(file.file.read())
    content={
        "cleaned": "True",
        "Filename": file.filename
    }
    return JSONResponse(status_code=status, content=content)
