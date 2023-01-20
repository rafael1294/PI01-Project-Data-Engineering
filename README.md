#            PROYECTO INDIVIDUAL #1 : DATA ENGINEER 

<p align="center">
<img src="https://www.esic.edu/sites/default/files/rethink/c7a84832-data-engineer.jpg"  height=250><br><br>

# Descripción del proyecto:

Construir una "API" para poder hacer consultas sobre las plataformas: 
- Amazon
- Disney 
- Hulu  
- Netflix<br><br>

# Proceso ETL:

- 1: El proceso ETL se ejecuta en el archivo "PI-01.ipynb". <br>

- 2: Los archivos "csv." en la carpeta "Datasets" son leidos y ejecutados por este archivo, luego son transformados y finalmente se genera archivo "csv." dentro de la carpeta "Tablas".<br><br>

# MySql:

<img src="https://www.redeszone.net/app/uploads-redeszone.net/2017/02/mysql-930x452.png"  height=100><br><br>

- Importamos la tabla a MySql y realizamos las querys para su comprobación. <br><br>

# PyMySql:

- Realizamos la conexión con la base de datos "PI1" desde python y generamos las consultas para su ejecución en la API.<br><br> 

# FastAPI:

<img src="https://cdn.sanity.io/images/6icyfeiq/production/e1027869dfe74b69acfcc4616199e50f3df1f52d-2800x1318.png?w=952&q=75&fit=max&auto=format&dpr=1"  height=100><br><br>

- El archivo "main.py" dentro de la carpeta "app" contiene todas las funciones que la aplicación necesita para realizar sus consultas a la base de datos.<br><br>

# Parámetros de la API:

- get_word_count: <br>
    Parametros: "plataforma","palabra"<br>
    Resultado: Cantidad de títulos que contienen la "palabra" en la "plataforma".<br>

- get_score count: <br>
        Parametros: "plataforma","score","año".<br>
        Resultado: Cantidad de títulos con una puntuación mayor a "score" en el "año" de la "plataforma".<br>

- get_second_score: <br>
    Parámetros: "plataforma".<br>
    Resultado: Segundo título con mayor score ordenado alfabéticamente en la "plataforma".<br>

- get_longest: <br>
    Parámetros: "plataforma","min o season","año"<br>
    Resultado: Título con la mayor duración en "min o season" del "año" en la "plataforma" .<br><br>

- get_rating_count: <br>
    Parámetros: "rating"<br>
    Resultado: Cantidad de títulos con "rating" en todas las plataformas.<br><br>

# Comprobación de resultados:

<img src="https://raw.githubusercontent.com/rafael1294/Project-Data-Engineering/main/Images/FastAPI.jpg"  height=300><br><br>