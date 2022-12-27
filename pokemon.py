import random

class Pokemon:
    def __init__(self, especie, level=random.randint(1, 100), nome=None ):
        self.especie = especie
        self.level = level
        if nome:
            self.nome = nome
        else:
            self.nome = especie



    def __str__(self):
        return f'{self.nome} ({self.level})'


    def atacar(self, pokemon):
        print(f'{self} atacou! {pokemon}')


class PokemonEletrico(Pokemon):
    tipo = 'eletrico'

    def atacar(self, pokemon):
        print(f'{self} lançou um choque do trovão em {pokemon}')


class PokemonFogo(Pokemon):
    tipo = 'fogo'

    def atacar(self, pokemon):
        print(f'{self} lançou uma bola de fogo na cabeça de {pokemon}' )


class PokemonAgua(Pokemon):
    tipo  = 'agua'

    def atacar(self, pokemon):
        print(f'{self} lançou um chato d`água em {pokemon}')














