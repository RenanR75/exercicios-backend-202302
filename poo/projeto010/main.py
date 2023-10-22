<<<<<<< HEAD
import fastapi

app = fastapi.FastAPI()

@app.get("/")
def indice():
    return{"mensagem" : "Ola Mundo."}

@app.get("/mundo")
def indiceMundo():
    return{"mensagem" : "Ola Todo Mundo."}
=======
import fastapi

app= fastapi.FastAPI()

@app.get("/")
def indice():
    return{"mensagem" : "Olá Mundo"}

@app.get("/mundo")
def indiceMundo():
     return{"mensagem" : "Olá todo mundo"}S
>>>>>>> e2ad4341a9b5e8ce59766eb3d00e19419a574b42
