from pydantic import BaseModel


class VideoBase(BaseModel):
    url : str
    


class VideoCreate(VideoBase):
    pass
    
    

class Video(VideoBase):
    id : int
    url : str
    
    
        
    class Config:
        orm_mode = True




class UserBase(BaseModel):
    name : str



class UserCreate(UserBase):
    name : str


class User(UserBase):
    id : int
    username : str
    videos : list[Video] = []
        
    class Config:
        orm_mode = True
