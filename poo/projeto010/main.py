import fastapi

app= fastapi.FastAPI()

@app.get("/")
def indice():
    return{"mensagem" : "Olá mundo"}