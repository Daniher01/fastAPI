from fastapi import FastAPI

app = FastAPI()

# ? para cambiar el nombre de la aplicacion
app.title = "Mi app  con FastApi"

# ? para cambiar la version de la app
app.version = "0.0.1"

# = los tags nos permite agrupar las rutas de la aplicacion
@app.get('/', tags=['home'])
def message():
    return "Hola mundo!"