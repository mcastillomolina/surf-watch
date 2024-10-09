from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True)

    surf_spots = relationship("UserSurfSpot", back_populates="user")

class SurfSpot(Base):
    __tablename__ = "surf_spots"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String, index=True)

    reports = relationship("SurfReport", back_populates="surf_spot")
    users = relationship("UserSurfSpot", back_populates="surf_spot")

class SurfReport(Base):
    __tablename__ = "surf_reports"

    id = Column(Integer, primary_key=True, index=True)
    surf_spot_id = Column(Integer, ForeignKey("surf_spots.id"))
    report_time = Column(DateTime)
    wave_height = Column(String)
    water_temperature = Column(String)
    wind_speed = Column(String)
    swell_direction = Column(String)

    surf_spot = relationship("SurfSpot", back_populates="reports")

class UserSurfSpot(Base):
    __tablename__ = "user_surf_spots"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    surf_spot_id = Column(Integer, ForeignKey("surf_spots.id"), primary_key=True)

    user = relationship("User", back_populates="surf_spots")
    surf_spot = relationship("SurfSpot", back_populates="users")
