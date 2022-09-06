from typing import List, Optional
from pydantic import BaseModel

class Owner(BaseModel):
    id: Optional[str]
    name: Optional[str]
    qtd_cars: Optional[int]
    colors: Optional[int]
    models: Optional[int]

# class Pessoa:
#     def __init__(self):
#         self.pessoa = None
#
#     def set_pessoa(self, owners):
#         pessoas = Owner(**{
#             "id": {"0": owners.id},
#             "name": {"0": owners.name},
#             "qtd_cars": {"0": owners.qtd_cars},
#             "colors": {"0": owners.models_cars},
#             "models": {"0": owners.colors_cars}
#         })
#         return pessoas