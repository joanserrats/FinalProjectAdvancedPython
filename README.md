# FinalProjectAdvancedPython
    Bienvenidos a mi trabajo final de Python Advanced, en él podreis encontrar un script que tiene como objetivo cargar, filtrar y analizar un dataset, en este caso un archivo .csv que contiene información acerca jugadores de la Bundesliga. 

## Installation

    pip install -r requirements.txt

## Usage
    python scripts/finalprojectadvancedpython.py -i dataset/BooksDatasetClean.csv

    Una vez cargado el dataset desde la ubicacion especifica, este podrá ser usado para aplicarle una serie de filtros con los que podremos averiguar informacion acerca de que jugadores son de nacionalidad alemana o cuales tienen mas de 30 años. 

## Test
    Para ejecutar los tests, usamos: 

    pytest


    Los tests se encuentran en test_sample.py y cubren varios escenarios para demostrar que el script de filtrado esta bien escrito. 
    Algunos de los que podemos encontrar son: 

        Filtrar jugadores mayores de edad: garantiza que los jugadores devueltos sean mayores que la edad especificada.

        Filtrar por Club: Verifica que los jugadores devueltos pertenecen al club especificado.

        Filtrar por nacionalidad: comprueba que los jugadores devueltos tengan la nacionalidad especificada.

        Filtrar jugadores por edad inexistente: prueba el caso en el que no se deben devolver jugadores por una edad inexistente.

        Filtrar por club inexistente: garantiza que no se devuelvan jugadores de un club inexistente.

