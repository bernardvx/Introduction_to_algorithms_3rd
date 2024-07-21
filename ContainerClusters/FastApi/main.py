from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session


from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


#Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#    db_user = crud.create_user(db, user=user)
 #   if db_user:
 #       raise HTTPException(status_code=400, detail="User already exists.")
    crud.create_user(db=db, user=user)
    return crud.create_user(db=db, user=user) #{"users_name": user.name, "username": user.username}#, "user_id": db_user.id}



@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user



@app.post("/users/{user_id}/videos", response_model=schemas.Video)
def post_video_for_user(user_id : int, video: schemas.VideoCreate, db: Session = Depends(get_db)):
    return crud.upload_video(db=db, video=video, user_id=user_id)

