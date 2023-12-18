from pydantic import BaseModel

class Graph_Request_Body(BaseModel):
    filePath: str
    src: str
    dest: str