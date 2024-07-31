from unittest import TestCase
from src.pokesdk.pokemon import Pokemon
import requests


class TestSDK(TestCase):
    def test_pokmeon_initialization(self):
        test_pokemon = Pokemon('https://pokeapi.co/api/v2/', requests.Session(), 20)
        self.assertEqual(test_pokemon.base_url, 'https://pokeapi.co/api/v2/pokemon')
        self.assertIsInstance(test_pokemon.client, requests.Session)
        self.assertEqual(test_pokemon.page_limit, 20)

    def test_pokemon_get_info_by_id(self):
        test_pokemon = Pokemon('https://pokeapi.co/api/v2/', requests.Session(), 20)
        pokemon = test_pokemon.get_info(1)
        self.assertEqual(pokemon.name, 'bulbasaur')

    def test_pokemon_get_info_bulk(self):
        test_pokemon = Pokemon('https://pokeapi.co/api/v2/', requests.Session(), 20)
        pokemon_list = test_pokemon.get_info()
        self.assertEqual(len(pokemon_list), 1302)

    def test_pokemon_get_info_bulk_large_page_limit(self):
        test_pokemon = Pokemon('https://pokeapi.co/api/v2/', requests.Session(), 10000)
        pokemon_list = test_pokemon.get_info()
        self.assertEqual(len(pokemon_list), 1302)
