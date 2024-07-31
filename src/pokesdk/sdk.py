from .pokemon import Pokemon
from .generation import Generation


BASE_URL = 'https://pokeapi.co/api/v2/'


class PokeSDK:
    """
        SDK for interfacing with PokeAPI v2
    """
    pokemon: Pokemon
    generation: Generation

    def __init__(self) -> None:
        self.pokemon = Pokemon(BASE_URL)
        self.generation = Generation(BASE_URL)
