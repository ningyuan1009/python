from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class RegisterResponse(BaseModel):
    message: str
    id: int
    username: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    message: str

class TokenData(BaseModel):
    username: str | None = None