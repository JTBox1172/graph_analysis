from pydantic import BaseModel
from fastapi import File, UploadFile
from typing import List

class Graph_Request_Body(BaseModel):
    filePath: str
    src: str
    dest: str