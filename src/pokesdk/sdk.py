from .pokemon import Pokemon
from .generation import Generation
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


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

        retry = Retry(
            total=5,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.client = requests.Session()
        self.client.mount('https://', adapter=adapter)

        self.page_limit = page_limit

        self.pokemon = Pokemon(BASE_URL, self.client, page_limit)
        self.generation = Generation(BASE_URL, self.client, page_limit)
