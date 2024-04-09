
from pydantic import BaseModel

class Request_User_Model(BaseModel):
    name:str
    email:str
    password:str
    


class Response_User_Model(BaseModel):
    id: int
    name: str
    email: str
    


class Login_Model(BaseModel):
    email: str
    password: str
    
class Request_Password_Change(BaseModel):
    email:str
    new_password: str