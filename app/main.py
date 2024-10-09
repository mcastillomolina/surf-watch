from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import schemas, crud
from .database import init_db, get_db
from typing import List
from api.routes import get_router

app = FastAPI(
    title='API to deliver your favorite surf spots reports to you!',
    description='Super awesome project for surfers',
    version='1.0.1'
)

init_db()

router = get_router()
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Surf Report Notification API. Yeeewww!!"}

@app.post("/surfspots/", response_model=schemas.SurfSpot)
def create_surf_spot(surf_spot: schemas.SurfSpotCreate, db: Session = Depends(get_db)):
    return crud.create_surf_spot(db=db, surf_spot=surf_spot)

@app.get("/surfspots/", response_model=List[schemas.SurfSpot])
def read_surf_spots(db: Session = Depends(get_db)):
    return crud.get_surf_spots(db=db)

@app.get("/surfspots/{surf_spot_id}", response_model=schemas.SurfSpot)
def read_surf_spot(surf_spot_id: int, db: Session = Depends(get_db)):
    db_surf_spot = crud.get_surf_spot(db=db, surf_spot_id=surf_spot_id)
    if db_surf_spot is None:
        raise HTTPException(status_code=404, detail="Surf spot not found")
    return db_surf_spot

@app.post("/users/{user_id}/surfspots/{surf_spot_id}", response_model=schemas.UserSurfSpot)
def link_user_surf_spot(user_id: int, surf_spot_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_surf_spot = crud.get_surf_spot(db=db, surf_spot_id=surf_spot_id)
    if db_surf_spot is None:
        raise HTTPException(status_code=404, detail="Surf spot not found")
    
    return crud.link_user_surf_spot(db=db, user_id=user_id, surf_spot_id=surf_spot_id)

@app.post("/surfspots/{surf_spot_id}/reports/", response_model=schemas.SurfReport)
def create_surf_report(surf_spot_id: int, surf_report: schemas.SurfReportCreate, db: Session = Depends(get_db)):
    db_surf_spot = crud.get_surf_spot(db=db, surf_spot_id=surf_spot_id)
    if db_surf_spot is None:
        raise HTTPException(status_code=404, detail="Surf spot not found")
    return crud.create_surf_report(db=db, surf_spot_id=surf_spot_id, surf_report=surf_report)

@app.get("/surfspots/{surf_spot_id}/reports/", response_model=List[schemas.SurfReport])
def read_surf_reports(surf_spot_id: int, db: Session = Depends(get_db)):
    db_surf_spot = crud.get_surf_spot(db=db, surf_spot_id=surf_spot_id)
    if db_surf_spot is None:
        raise HTTPException(status_code=404, detail="Surf spot not found")
    return crud.get_surf_reports(db=db, surf_spot_id=surf_spot_id)
