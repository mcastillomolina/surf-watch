from sqlalchemy.orm import Session
from . import models, schemas

# User operations
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email, phone_number=user.phone_number)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# SurfSpot operations
def create_surf_spot(db: Session, surf_spot: schemas.SurfSpotCreate):
    db_surf_spot = models.SurfSpot(name=surf_spot.name, location=surf_spot.location)
    db.add(db_surf_spot)
    db.commit()
    db.refresh(db_surf_spot)
    return db_surf_spot

def get_surf_spots(db: Session):
    return db.query(models.SurfSpot).all()

def get_surf_spot(db: Session, surf_spot_id: int):
    return db.query(models.SurfSpot).filter(models.SurfSpot.id == surf_spot_id).first()

# Link user to surf spot
def link_user_surf_spot(db: Session, user_id: int, surf_spot_id: int):
    db_link = models.UserSurfSpot(user_id=user_id, surf_spot_id=surf_spot_id)
    db.add(db_link)
    db.commit()
    return db_link

# SurfReport operations
def create_surf_report(db: Session, surf_spot_id: int, surf_report: schemas.SurfReportCreate):
    db_surf_report = models.SurfReport(
        surf_spot_id=surf_spot_id,
        report_time=surf_report.report_time,
        wave_height=surf_report.wave_height,
        water_temperature=surf_report.water_temperature,
        wind_speed=surf_report.wind_speed,
        swell_direction=surf_report.swell_direction
    )
    db.add(db_surf_report)
    db.commit()
    db.refresh(db_surf_report)
    return db_surf_report

def get_surf_reports(db: Session, surf_spot_id: int):
    return db.query(models.SurfReport).filter(models.SurfReport.surf_spot_id == surf_spot_id).all()
