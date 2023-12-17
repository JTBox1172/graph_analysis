from pydantic import BaseModel

class retrievalBody(BaseModel):
    filePath: str
    fileName: str