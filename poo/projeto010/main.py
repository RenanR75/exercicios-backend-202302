import fastapi

app= fastapi.FastAPI()

@app.get("/")
def indice():
    return{"mensagem" : "Olá mundo"}

@app.get("/mundo")
def indiceMundo():
     return{"mensagem" : "Olá todo mundo"}