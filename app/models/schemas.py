from typing import List
from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str
    
class BatchRequest(BaseModel):
    texts: List[str]