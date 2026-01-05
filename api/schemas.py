from pydantic import BaseModel
from typing import List

class ProxyItem(BaseModel):
    id: str
    type: str

class ProxyData(BaseModel):
    list: List[ProxyItem]

class ProxyResponse(BaseModel):
    data: ProxyData