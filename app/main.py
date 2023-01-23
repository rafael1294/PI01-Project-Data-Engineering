from fastapi import FastAPI
from starlette.responses import RedirectResponse
import pymysql

app = FastAPI()


def conectar_a_base_de_datos() :
    conexion = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mysql123M',
    db= 'pi1',
    port= 3306
    )
    return conexion.cursor()


#1 Funcion: Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
def word_count(plataforma,kword):
    cursor=conectar_a_base_de_datos()
    a=[]
    plataforma=str(plataforma)
    kword=str(kword)
    p=''
    if plataforma == "amazon":
        p = "a"
    elif plataforma == "disney":
        p = "d"
    elif plataforma == "hulu":
        p = "h"
    elif plataforma == "netflix":
        p = "n"
    else:
        "Inserte: amazon, disney, hulu o netflix"
    
    cursor.execute("select id_plataform, title, count(*) as cantidad \
        from dftitle \
        where title like '%"+kword+"%' and id_plataform = '"+p+"'")
        
    for dato in cursor:
        a.append(dato)
    
    return a
    


#2 Funcion: Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
def score_count(plataforma,score,year):
    cursor=conectar_a_base_de_datos()
    a=[]
    score=str(score)
    year=str(year)
    p=''
    if plataforma == "amazon":
        p = "a"
    elif plataforma == "disney":
        p = "d"
    elif plataforma == "hulu":
        p = "h"
    elif plataforma == "netflix":
        p = "n"
    else:
        "Inserte: amazon, disney, hulu o netflix"
    
    cursor.execute("select id_plataform, title, count(*) as cantidad \
        from dftitle\
        where score > '"+score+"' and id_plataform = '"+p+"' and release_year = '"+year+"' and type ='movie'")
    
    for dato in cursor:
        a.append(dato)
    
    return a
    
#3 Funcion: La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
def second_score(plataforma):
    cursor=conectar_a_base_de_datos()
    a=[]
    p=''
    if plataforma == "amazon":
        p = "a"
    elif plataforma == "disney":
        p = "d"
    elif plataforma == "hulu":
        p = "h"
    elif plataforma == "netflix":
        p = "n"
    else:
        "Inserte: amazon, disney, hulu o netflix"
    query="select * from (select id_plataform, score, title, ROW_NUMBER() OVER (ORDER BY score desc, title) AS orden \
        from dftitle) a \
        where id_plataform = '"+p+"' and orden = 2"
    cursor.execute(query)

    for dato in cursor:
        a.append(dato)
    
    return a
    

#4 Funcion: Película que más duró según año, plataforma y tipo de duración
def longest(plataforma,tip,year):
    cursor=conectar_a_base_de_datos()
    a=[]
    year=str(year)
    p=''
    if plataforma == "amazon":
        p = "a"
    elif plataforma == "disney":
        p = "d"
    elif plataforma == "hulu":
        p = "h"
    elif plataforma == "netflix":
        p = "n"
    else:
        "Inserte: amazon, disney, hulu o netflix"
    
    query="select id_plataform, title, release_year, convert(SUBSTRING_INDEX(duration,' ', 1), UNSIGNED INTEGER)  AS tiempo,\
        SUBSTRING_INDEX(duration,' ', -1) as unidades from dftitle \
        where release_year = '"+year+"' and id_plataform = '"+p+"' and SUBSTRING_INDEX(duration,' ', -1) like '"+tip+"%' \
        order by 4 desc \
        limit 1"
    cursor.execute(query)

    for dato in cursor:
        a.append(dato)
    
    return a

#5 Funcion: Cantidad de series y películas por rating
def rating_count(rating):
    cursor=conectar_a_base_de_datos()
    a=[]
     
    query="select rating, type, count(*) as cantidad \
        from dftitle \
        where rating ='"+rating+"' \
        group by rating"
    cursor.execute(query)

    for dato in cursor:
        a.append(dato)
    
    return a

#uvicorn main:app --reload para iniciar servidor
@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

@app.get("/get_word_count({plataforma},{kword})")  
async def titulos(plataforma:str,kword:str):
     return {"En la plataforma "+plataforma+" los titulos que poseen la palabra "+kword+" son " : word_count(plataforma,kword)[0][2]}

@app.get("/get_score_count({plataforma},{score},{year})") 
async def cantidad(plataforma:str,score:int,year:int):
    x = str(score)
    return {"La cantidad de peliculas con score mayor a "+x+" en la plataforma "+plataforma+" son" : score_count(plataforma,score,year)[0][2]}

@app.get("/get_second_score({plataforma})") 
async def second(plataforma:str):
    return {"La segunda película con mayor score en la plataforma "+plataforma+" es" : second_score(plataforma)[0][2]}

@app.get("/get_longest({plataforma},{tip},{year})") 
async def long(plataforma:str,tip:str,year:int):
    return {"La película con mayor duración en '"+tip+"' de la plataforma "+plataforma+" es" : longest(plataforma,tip,year)[0][1],
            "con un valor de" : longest(plataforma,tip,year)[0][3]}

@app.get("/get_rating_count({rating})") 
async def ratng(rating:str):
    return {"La cantidad de 'títulos' en todas las plataformas, con un rating de '"+rating+"' son" : rating_count(rating)[0][2]}



