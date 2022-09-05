from typing import List, Optional
from pydantic import BaseModel

class Car(BaseModel):
    id: str
    colors: Optional[int]
    models: Optional[int]
    id_owner: Optional[str]