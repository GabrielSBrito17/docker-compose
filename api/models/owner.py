from typing import List, Optional
from pydantic import BaseModel

class Owner(BaseModel):
    id: str
    colors: int
    models: int