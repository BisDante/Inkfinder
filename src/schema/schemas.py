from pydantic import BaseModel
from typing import Optional
import datetime

class Entity(BaseModel):
    id : Optional[str]
    name : str

    class Config:
        orm_mode = True


class Appointment(BaseModel):
    date_time : datetime.datetime
    estimate_duration = datetime.time
    tattoo_id : str
    price = float
    tattoo_artist_id : str
    studio_id : str
    confirmed : Optional[bool] = False


class Person(Entity):
    surname : str
    username : str
    password : str
    email : str
    history : str
    appointments : str
    artist : bool


class PersonNoPass(Entity):
    surname : str
    username : str
    history : str
    appointments : str
    artist : bool


class Tattoo(BaseModel):
    id : Optional[str] = None
    picture : str
    name : str
    description : str
    studio_id : str
    tags : int


class Post(BaseModel):
    id : Optional[str] = None
    text : str
    picture : str
    tattoo_artist_id : str
    likes : int


class Studio(Entity):
    artists : int
    address : str
    posts : int


class Login(BaseModel):
    username : str
    password : str