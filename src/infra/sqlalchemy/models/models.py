from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Time
from src.infra.sqlalchemy.config.database import Base


class Appointment(Base):
    __tablename__ = 'Appointments'
    id = Column(String, primary_key=True, index = True)
    date_time = Column(String)
    estimate_duration = Column(String)
    tattoo_id = Column(String)
    price = Column(Float)
    tattoo_artist_id = Column(String)
    studio_id = Column(String)
    confirmed = Column(Boolean)


class Person(Base):
    __tablename__ = 'People'
    id = Column(String, primary_key=True, index = True)
    name = Column(String)
    surname = Column(String)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    history = Column(String)
    appointments = Column(String)
    artist = Column(Boolean)


class Tattoo(Base):
    __tablename__ = 'Tattoos'
    id = Column(String, primary_key=True, index=True)
    picture = Column(String)
    name = Column(String)
    description = Column(String)
    studio_id = Column(String)
    tags = Column(Integer)


class Post(Base):
    __tablename__ = 'Posts'
    id = Column(String, primary_key=True, index=True)
    text = Column(String)
    picture = Column(String)
    tattoo_artist_id = Column(String)
    likes = Column(Integer)


class Studio(Base):
    __tablename__ = 'Studios'
    id = Column(String, primary_key=True, index = True)
    name = Column(String)
    artists = Column(Integer)
    address = Column(String)
    posts = Column(Integer)


