from typing import List, Optional
from pydantic import BaseModel

class Owner(BaseModel):
    id: str
    name: Optional[str]
    qtd_cars: Optional[int]
    colors: Optional[int]
    models: Optional[int]
