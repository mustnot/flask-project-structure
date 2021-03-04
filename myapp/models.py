from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: Optional[str] = "guest"
    age: int = 99
