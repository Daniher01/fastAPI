from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()

# ? para cambiar el nombre de la aplicacion
app.title = "Mi app  con FastApi"

# ? para cambiar la version de la app
app.version = "0.0.1"

#! listado de peliculas
movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } ,
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]

# ? los tags nos permite agrupar las rutas de la aplicacion
@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1 style=color:red> hola mundo </h1>')


@app.get('/movies', tags = ['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags = ['movies'])
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []    

@app.get('/movies/', tags = ['movies'])
def get_movies_by_category(category: str):
    return [ item for item in movies if item["category"] == category]


@app.post('/movies', tags = ['movies'])
def create_movies(id:int = Body(), title:str = Body(), overview:str = Body(), year:int = Body(), rating:float = Body(), category:str = Body()):
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year":year,
        "rating": rating,
        "category": category
    })
    return movies