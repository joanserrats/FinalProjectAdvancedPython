"""
Scripts to make basic filters
"""

import pandas as pd
import click
import pdb 


def load_dataset(bundeslig_player):
    """
    function to load dataset
    """
    extension = bundeslig_player.rsplit('.', 1)[-1]
    if extension == "csv":
        return pd.read_csv(bundeslig_player)
    else:
        raise TypeError(f"The extension is {extension} and not csv. Try again")


class PlayerFilter:
    def __init__(self, file_name):
        # Cargar el dataset con un manejo básico de errores
        try:
            self.data = pd.read_csv(file_name)
        except FileNotFoundError:
            print(f"El archivo {file_name} no se encontró.")
            self.data = None
        except pd.errors.EmptyDataError:
            print("El archivo está vacío.")
            self.data = None
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
            self.data = None

    def filter_players_over_age(self, age_threshold=30):
        # Filtra jugadores mayores de la edad especificada
        players_over_age = self.data[self.data['age'] > age_threshold]
        return players_over_age[['name', 'age', 'club']]

    def filter_by_club(self, club_name):
        # Filtra jugadores por el nombre del club
        return self.data[self.data['club'] == club_name][['name', 'age', 'club']]

    def filter_by_nationality(self, nationality):
        # Filtra jugadores por nacionalidad
        return self.data[self.data['nationality'] == nationality][['name', 'age', 'nationality']]

@click.command()
@click.option('-f', '--file_name', required=True, help='File to import')
def main(file_name):
    """
    Main function 
    """
    #inicio debugging para en caso de que haya error lo detecte
    pdb.set_trace()

    player_filter = PlayerFilter(file_name)
    
    # Filtra jugadores mayores de 30 años
    print("Jugadores mayores de 30 años:")
    print(player_filter.filter_players_over_age(30))
    
    # Filtra jugadores del club 'Bayern Munich' 
    print("\nJugadores del Bayern Munich:")
    print(player_filter.filter_by_club('Bayern Munich'))
    
    # Filtra jugadores de nacionalidad 'Germany' 
    print("\nJugadores de nacionalidad alemana:")
    print(player_filter.filter_by_nationality('Germany'))

if __name__ == '__main__':
    print("Test")
    main()