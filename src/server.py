from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, create_db
from src.schema.schemas import *
from src.infra.repos.repos import *


create_db()
app = FastAPI()

origins = ["http://localhost:5500"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get('/people', status_code=200, response_model=List[PersonNoPass])
def list_people(db : Session = Depends(get_db)):
    people = PersonRepo(db).list_people()
    return people


@app.get('/people/{id}', status_code=200, response_model=PersonNoPass)
def get_person(id : str, db : Session = Depends(get_db)):
    person = PersonRepo(db).get(id)
    return person


@app.post('/people', status_code=201, response_model=PersonNoPass)
def create_person(person : schemas.Person, db : Session = Depends(get_db)):
    new_person = PersonRepo(db).create(person)
    return new_person


@app.put('/people')
def edit_person(person : schemas.Person, db : Session = Depends(get_db)):
    edit_person = PersonRepo(db).update(person)
    return "atualizado com sucesso!"


@app.delete('/people{id}')
def create_person(person : schemas.Person, db : Session = Depends(get_db)):
    person = PersonRepo(db).remove(id)

@app.get('/tattoos', status_code=200, response_model=List[schemas.Tattoo])
def list_tattoos(db : Session = Depends(get_db)):
    tattoos = TattooRepo(db).list_tattoos()
    return tattoos


@app.get('/tattoos/{id}', status_code=200, response_model=schemas.Tattoo)
def get_tattoo(id : str, db : Session = Depends(get_db)):
    tattoo = TattooRepo(db).get(id)
    return tattoo


@app.post('/tattoos', status_code=201, response_model=schemas.Tattoo)
def create_tattoo(tattoo : schemas.Tattoo, db : Session = Depends(get_db)):
    new_tattoo = TattooRepo(db).create(tattoo)
    return new_tattoo


@app.put('/tattoos')
def edit_tattoo(tattoo : schemas.Tattoo, db : Session = Depends(get_db)):
    edit_tattoo = TattooRepo(db).update(tattoo)
    return "atualizado com sucesso!"


@app.delete('/tattoos{id}')
def create_tattoo(tattoo : schemas.Tattoo, db : Session = Depends(get_db)):
    tattoo = TattooRepo(db).remove(id)


@app.get('/appointments', status_code=200, response_model=List[schemas.Appointment])
def list_appointments(db : Session = Depends(get_db)):
    appointments = AppointmentRepo(db).list_appointments()
    return appointments


@app.get('/appointments/{id}', status_code=200, response_model=schemas.Appointment)
def get_appointment(id : str, db : Session = Depends(get_db)):
    appointment = AppointmentRepo(db).get(id)
    return appointment


@app.post('/appointments', status_code=201, response_model=schemas.Appointment)
def create_appointment(appointment : schemas.Appointment, db : Session = Depends(get_db)):
    new_appointment = AppointmentRepo(db).create(appointment)
    return new_appointment


@app.put('/appointments')
def edit_appointment(appointment : schemas.Appointment, db : Session = Depends(get_db)):
    edit_appointment = AppointmentRepo(db).update(appointment)
    return "atualizado com sucesso!"


@app.delete('/appointments{id}')
def create_appointment(appointment : schemas.Appointment, db : Session = Depends(get_db)):
    appointment = AppointmentRepo(db).remove(id)


@app.get('/studios', status_code=200, response_model=List[schemas.Studio])
def list_studios(db : Session = Depends(get_db)):
    studios = StudioRepo(db).list_studios()
    return studios


@app.get('/studios/{id}', status_code=200, response_model=schemas.Studio)
def get_studio(id : str, db : Session = Depends(get_db)):
    studio = StudioRepo(db).get(id)
    return studio


@app.post('/studios', status_code=201, response_model=Studio)
def create_studio(studio : schemas.Studio, db : Session = Depends(get_db)):
    new_studio = StudioRepo(db).create(studio)
    return new_studio


@app.put('/studios')
def edit_studio(studio : schemas.Studio, db : Session = Depends(get_db)):
    edit_studio = StudioRepo(db).update(studio)
    return "atualizado com sucesso!"


@app.delete('/studios{id}')
def create_studio(studio : schemas.Studio, db : Session = Depends(get_db)):
    studio = StudioRepo(db).remove(id)


@app.get('/posts', status_code=200, response_model=List[schemas.Post])
def list_posts(db : Session = Depends(get_db)):
    posts = PostRepo(db).list_posts()
    return posts


@app.get('/posts/{id}', status_code=200, response_model=schemas.Post)
def get_post(id : str, db : Session = Depends(get_db)):
    post = PostRepo(db).get(id)
    return post


@app.post('/posts', status_code=201, response_model=schemas.Post)
def create_post(post : schemas.Post, db : Session = Depends(get_db)):
    new_post = PostRepo(db).create(post)
    return new_post


@app.put('/posts')
def edit_post(post : schemas.Post, db : Session = Depends(get_db)):
    edit_post = PostRepo(db).update(post)
    return "atualizado com sucesso!"


@app.delete('/posts{id}')
def create_post(post : schemas.Post, db : Session = Depends(get_db)):
    post = PostRepo(db).remove(id)


@app.post('/login')
def login(login : schemas.Login, db : Session = Depends(get_db)):
    user = PersonRepo(db).Login(login)
    return user