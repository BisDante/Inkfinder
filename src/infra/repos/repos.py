from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from src.schema import schemas
from src.infra.sqlalchemy.models import models
from uuid import uuid4


class PersonRepo():
    def __init__(self, db : Session = None):
        self.db = db


    def create(self, person : schemas.Person):
        new_person = models.Person(id=str(uuid4()),
                                   name=person.name,
                                   surname=person.surname,
                                   username=person.username,
                                   password=person.password,
                                   email=person.email,
                                   history=person.history,
                                   appointments=person.appointments,
                                   artist=person.artist)
        self.db.add(new_person)
        self.db.commit()
        self.db.refresh(new_person)
        return new_person


    def list_people(self):
        people = self.db.query(models.Person).all()
        return people


    def get(self, person_id):
        person = self.db.query(models.Person).get(person_id)

        return person


    def remove(self, person_id):
        statement = delete(models.Person).where(models.Person.id == person_id)

        self.db.execute(statement)
        self.db.commit()


    def update(self, person : schemas.Person):
        statement = update(models.Person).where(models.Person.id==person.id).values(name=person.name,
                                                                                    surname=person.surname,
                                                                                    username=person.username,
                                                                                    password=person.password,
                                                                                    email=person.email,
                                                                                    history=person.history,
                                                                                    appointments=person.appointments,
                                                                                    artist=person.artist)
        self.db.execute(statement)
        self.db.commit()


    def Login(self, login : schemas.Login):
        statement = self.db.query(models.Person).where((and_(models.Person.username == login.username,
                                                        models.Person.password == login.password)))
        user = self.db.execute(statement).one()
        if user != None: return "Login efetuado com sucesso!"
        else: return None


class StudioRepo():
    def __init__(self, db : Session = None):
        self.db = db


    def create(self, studio : schemas.Studio):
        new_studio = models.Studio(id=str(uuid4()),
                                   name=studio.name,
                                   artists=studio.artists,
                                   address=studio.address,
                                   posts=studio.posts)
        self.db.add(new_studio)
        self.db.commit()
        self.db.refresh(new_studio)
        return new_studio


    def list_studios(self):
        studios = self.db.query(models.Studio).all()
        return studios


    def get(self, studio_id):
        statement = select(models.Studio).filter_by(id=studio_id)
        studio = self.db.execute(statement).one()

        return studio


    def remove(self, studio_id):
        statement = delete(models.Studio).where(models.Studio.id == studio_id)

        self.db.execute(statement)
        self.db.commit()


    def udpate(self, studio):
        statement = update(models.Studio).where(models.Studio.id == studio.id).values(name=studio.name,
                                                                                    artists=studio.artists,
                                                                                    address=studio.address,
                                                                                    posts=studio.posts)
        self.db.execute(statement)
        self.db.commit()


class PostRepo():
    def __init__(self, db : Session = None):
        self.db = db


    def create(self, post : schemas.Post):
        new_post = models.Post(id=str(uuid4()),
                                name=post.name,
                                artists=post.artists,
                                address=post.address,
                                posts=post.posts)
        self.db.add(new_post)
        self.db.commit()
        self.db.refresh(new_post)
        return new_post


    def list_posts(self):
        posts = self.db.query(models.Post).all()
        return posts


    def get(self, post_id):
        statement = select(models.Post).filter_by(id=post_id)
        post = self.db.execute(statement).one()

        return post


    def remove(self, post_id):
        statement = delete(models.Post).where(models.Post.id == post_id)

        self.db.execute(statement)
        self.db.commit()


    def update(self, post):
        statement = update(models.Post).where(models.Post.id == post.id).values(name=post.name,
                                                                                artists=post.artists,
                                                                                address=post.address,
                                                                                posts=post.posts)
        self.db.execute(statement)
        self.db.commit()


class TattooRepo():
    def __init__(self, db : Session = None):
        self.db = db


    def create(self, tattoo : schemas.Tattoo):
        new_tattoo = models.Tattoo(id=str(uuid4()),
                                   picture=tattoo.picture,
                                   name=tattoo.name,
                                   description=tattoo.description,
                                   studio_id=tattoo.studio_id,
                                   tags=tattoo.tags)
        self.db.add(new_tattoo)
        self.db.commit()
        self.db.refresh(new_tattoo)
        return new_tattoo


    def list_tattoos(self):
        tattoos = self.db.query(models.Tattoo).all()
        return tattoos


    def get(self, tattoo_id):
        filter = select(models.Tattoo).filter_by(id=tattoo_id)
        tattoo = self.db.execute(filter).one()

        return tattoo


    def remove(self, tattoo_id):
        statement = delete(models.Tattoo).where(models.Tattoo.id == tattoo_id)

        self.db.execute(statement)
        self.db.commit()


    def update(self, tattoo : models.Tattoo):
        statement = update(models.Tattoo).where(models.Tattoo.id == tattoo.id).values(picture=tattoo.picture,
                                                                                    name=tattoo.name,
                                                                                    description=tattoo.description,
                                                                                    studio_id=tattoo.studio_id,
                                                                                    tags=tattoo.tags)
        self.db.execute(statement)
        self.db.commit()


class AppointmentRepo():
    def __init__(self, db : Session = None):
        self.db = db


    def create(self, appointment : schemas.Appointment):
        new_appointment = models.Appointment(id=str(uuid4()),
                                   date_time=appointment.date_time,
                                   tattoo_id=appointment.tattoo_id,
                                   price=appointment.price,
                                   tattoo_artist_id=appointment.tattoo_artist_id,
                                   studio_id=appointment.studio_id,
                                   confirmed=appointment.confirmed)
        self.db.add(new_appointment)
        self.db.commit()
        self.db.refresh(new_appointment)
        return new_appointment


    def list_appointments(self):
        appointments = self.db.query(models.Appointment).all()
        return appointments


    def get(self, appointment_id):
        filter = select(models.Appointment).filter_by(id=appointment_id)
        appointment = self.db.execute(filter).one()

        return appointment


    def remove(self, appointment_id):
        statement = delete(models.Appointment).where(models.Appointment.id == appointment_id)

        self.db.execute(statement)
        self.db.commit()

    
    def update(self, appointment : models.Appointment):
        statement = update(models.Appointment).where(models.Appointment.id == appointment.id).values(date_time=appointment.date_time,
                                                                                                    tattoo_id=appointment.tattoo_id,
                                                                                                    price=appointment.price,
                                                                                                    tattoo_artist_id=appointment.tattoo_artist_id,
                                                                                                    studio_id=appointment.studio_id,
                                                                                                    confirmed=appointment.confirmed)