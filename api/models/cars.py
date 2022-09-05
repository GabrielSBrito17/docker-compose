from typing import List, Optional
from pydantic import BaseModel

class Car(BaseModel):
    id: str
    colors: int
    models: int
    id_owner: str