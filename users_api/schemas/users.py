from pydantic import BaseModel, Field
class UserCreate(BaseModel):
    username: str           #вход данные  |   pydantic
    surname: str
    age: int = Field(ge = 0)

class UserResponse(BaseModel):
    id: int
    username: str              #вывод данных |  pydantic
    name: str
    surname: str
    age: int


    model_config = {'from_attributes': True}

