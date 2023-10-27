import fastapi, connection
app = fastapi.FastAPI()
@app.get("/")
def hello_world_root():
    return {"Olá": "Funciona"}

@app.get("/getContinents")
def getContinents():
    Continents_list = []
    mycursor= connection.mydb.cursor(dictionary=True)
    for data_continents in mycursor:
        Continents_list.append(data_continents)
    mycursor.close()
    return {"Continents": Continents_list}

