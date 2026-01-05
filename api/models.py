from pydantic import BaseModel, Field
from typing import List, Optional

# class Item(BaseModel):
#     id: str

# class DataList(BaseModel):
#     list: List[Item]

# async def get_data():
#     raw_data = {'data': {'list': [{'id': 'hello'}]}}

# Структура для /items
class Item(BaseModel):
    id: str
    price: int

class ItemsResponse(BaseModel):
    items: List[Item] = Field(alias="list") # Если в JSON ключ "list", а мы хотим поле "items"

# Структура для /users
class User(BaseModel):
    id: int
    username: str

class UsersResponse(BaseModel):
    users: List[User] = Field(alias="data")

    try:
        response = ApiResponse(**raw_data)
        first_id = response.data.list[0].id
        return first_id
    except (IndexError, ValueError):
        return None