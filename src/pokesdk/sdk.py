from .pokemon import Pokemon
from .generation import Generation
import requests


BASE_URL = 'https://pokeapi.co/api/v2/'


class PokeSDK:
    """
        SDK for interfacing with PokeAPI v2
    """
    client: requests.Session
    page_limit: int
    pokemon: Pokemon
    generation: Generation

    def __init__(self, page_limit=20):

        self.client = requests.Session()
        self.page_limit = page_limit

        self.pokemon = Pokemon(BASE_URL, self.client, page_limit)
        self.generation = Generation(BASE_URL, self.client, page_limit)
