from pydantic import BaseModel


class VideoBase(BaseModel):
    url : str
    


class VideoCreate(VideoBase):
    url : str
    
    

class Video(VideoBase):
    id : int
    
    
        
    class Config:
        orm_mode = True




class UserBase(BaseModel):
    name : str



class UserCreate(UserBase):
    username : str


class User(UserBase):
    id : int
    username : str
    videos : list[Video] = []
        
    class Config:
        orm_mode = True
