import fastapi

app = fastapi.FastAPI()

@app.get("/")
def indice():
    return{"mensagem" : "Ola Mundo."}

@app.get("/mundo")
def indiceMundo():
    return{"mensagem" : "Ola Todo Mundo."}

@app.get("/marte")
def indiceMartee( nome_planeta: str = fastapi.Path(..., description="Preencha com o nome do planeta")):
    return{"mensagem" : "Olá residentes da Terra."}
