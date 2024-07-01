from sqlalchemy.orm import Session
from . import models, schemas
import random

def get_user(db : Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()





def create_user(db: Session, user: schemas.UserCreate):
    generated_username = user.name + str(random.randint(0, 3000))
    db_user = models.User(name=user.name, username=generated_username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user




def upload_video(db: Session, video: schemas.VideoCreate, user_id: int):
    db_video = models.Videos(url=video.url, owner_id = user_id)
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video



