from enum import Enum
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

class Entity(BaseModel):
    
    id : Optional[uuid4]

    def __init__(self, name):
        self._name = name
        
    
    def get_name(self):
        return self._name
    

    def set_name(self, name):
        self._name = name


class Tags(Enum):
    POINTILLISM = 0
    OLD_SCHOOL = 1
    GEOMETRIC = 2
    MINIMALIST = 3
    BLACKWORK = 4
    SINGLE_LINE = 5
    GLITCH = 6
    WHITE_INK = 7
    RED_INK = 8
    BLACK_AND_WHITE = 9
    NO_CONTOUR = 10
    WATERCOLOR = 11
    ORIENTAL = 12
    REALISTIC = 13
    MAORI = 14


class Appointment(BaseModel):

    def __init__(self, date, time, estimate_duration, tattoo, price, tattoo_artist):
        self._date = date
        self._time = time
        self._estimate_duration = estimate_duration
        self._tattoo = tattoo
        self._price = price
        self._tattoo_artist = tattoo_artist
        self._confirmed = False


    def set_confirmed(self, confirmed):
        self._confirmed = confirmed


class Person(Entity):
    def __init__(self, name, surname, username, password, email, picture):
        super().__init__(name, picture)
        self._surname = surname
        self._username = username
        self._password = password
        self._email = email
        self._history = []
        self._appointments = []
        

    def get_surname(self):
        return self._surname
    

    def set_surname(self, surname):
        return self._surname


    def get_username(self):
        return self._username


    def set_username(self, username):
        self._username = username


    def get_password(self):
        return self._password
    

    def set_password(self, password):
        self._password = password


    def get_email(self):
        return self._email
    

    def set_email(self, email):
        self._email = email


    def get_picture(self):
        return self._picture


    def set_picture(self, picture):
        self._picture = picture
    

    def get_history(self):
        return self._history
    

    def add_to_history(self, appointment):
        self._history.append(appointment)
    

    def get_appointments(self):
        return self._appointments
    

    def add_appointment(self, appointment):
        self._appointments.append(appointment)


    def cancel_appointment(self, appointment : Appointment):
        if appointment in self._appointments:
            appointment.set_confirmed(False)
            self._appointments.remove(appointment)

    
    def reschedule_appointment(self, appointment : Appointment, date, time):
        appointment.set_date(date)
        appointment.set_time(time)
        appointment.set_confirmed(False)


class Client(Person):
    def __init__(self, name, surname, picture):
        super().__init__(name, surname, picture)


    def create_appointment(self, date, tattoo, price, tattoo_artist):
        appointment = Appointment(date, tattoo, price, tattoo_artist)
        self._appointments.append(appointment)


class TattooArtist(Person):
    def __init__(self, name, surname, picture):
        super().__init__(name, surname, picture)
        self._posts = []

    def confirm_appointment(appointment):
        appointment.confirmed = True
            
        
    def create_post(self, text, picture):
        post = Post(text, picture, self)
        self._posts.append(post)


class Tattoo(BaseModel):
    def __init__(self, picture, name, description, tags):
        self._picture = picture
        self._name = name
        self._description = description
        self._tags = tags 


class Studio(BaseModel):
    def __init__(self, artists, address):
        self.artists = artists
        self.address = address
        self.posts = []


class Post(BaseModel):
    def __init__(self, text, picture, tattoo_artist):
        self._text = text
        self._picture = picture
        self._tattoo_artist = tattoo_artist
        self.likes = 0