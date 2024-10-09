from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: str
    phone_number: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    surf_spots: List["UserSurfSpot"] = []

    class Config:
        orm_mode = True

class SurfSpotBase(BaseModel):
    name: str
    location: str

class SurfSpotCreate(SurfSpotBase):
    pass

class SurfSpot(SurfSpotBase):
    id: int
    reports: List["SurfReport"] = []
    users: List["UserSurfSpot"] = []

    class Config:
        orm_mode = True

class SurfReportBase(BaseModel):
    report_time: datetime
    wave_height: str
    water_temperature: str
    wind_speed: str
    swell_direction: str

class SurfReportCreate(SurfReportBase):
    pass

class SurfReport(SurfReportBase):
    id: int
    surf_spot_id: int

    class Config:
        orm_mode = True

class UserSurfSpot(BaseModel):
    user_id: int
    surf_spot_id: int

    class Config:
        orm_mode = True
