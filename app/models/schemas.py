from typing import List
from pydantic import BaseModel

class BatchRequest(BaseModel):
    texts: List[str]