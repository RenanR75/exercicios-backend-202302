import fastapi, connection
app = fastapi.FastAPI()

@app.get("/")
def hello_world_root():
    return {"Olá": "Funciona"}

@app.get("/getregion")
def getregion():
    region = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql = "select * from region"
    mycursor.execute(sql)
    for region in mycursor:
        region_id.append( region )
    mycursor.close()
    return {"regions": region_id}

@app.get("/getContinents/{continent_id}")
def getContinents(continent_id : int):
    Continents_list = []
    mycursor= connection.mydb.cursor(dictionary=True)
    sql="select * from continents where continent_id = {0}".format(continent_id)
    mycursor.execute(sql)
    for data_continents in mycursor:
        Continents_list.append(data_continents)
    mycursor.close()
    return {"Continents": Continents_list}

@app.get("/getRegions")
def getRegions():
    Regions_list = []
    mycursor = connection.mydb.cursor(dictionary=True)
    sql = "select * from regions"
    mycursor.execute(sql)
    for data_regions in mycursor:
        Regions_list.append( data_regions )
    mycursor.close()
    return {"Regions": Regions_list}

@app.get("/getRegion/{continent_id}")
def getRegion(continent_id : int):
    Continents_list = []
    mycursor= connection.mydb.cursor(dictionary=True)
    sql="select * from continents where continent_id = {0}".format(continent_id)
    mycursor.execute(sql)
    for data_regions in mycursor:
        Continents_list.append(data_regions)
    mycursor.close()
    return {"regions": regions_list}
