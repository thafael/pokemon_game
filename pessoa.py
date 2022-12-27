# from pokemon import Pokemon, PokemonEletrico, PokemonFogo, PokemonAgua OU
from pokemon import *
import random

NOMES = [
    'João', 'Isabela', 'Lorena', 'Francisco', 'Ricardo', 'Diego',
    'Patrícia', 'Marcelo', 'Gustavo', 'Gerônimo', 'Gary'
]

POKEMONS = [
    
]


class Pessoa:

    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        print(f'Pokemons de {self}:')
        if self.pokemons:
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print(f'{self} não tem nenhum pokemon')



class Player(Pessoa):
    tipo = 'player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f'{self} capturou {pokemon}!')


class Inimigo(Pessoa):
    tipo = 'inimigo'

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            pokemons =

        super().__init__(nome=nome, pokemons=pokemons)



eu = Player()
print(eu)
meu_pokemon = PokemonFogo('charmander', level=1)
print(meu_pokemon)




