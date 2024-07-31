from unittest import TestCase
from src.pokesdk.generation import Generation
import requests


class TestSDK(TestCase):
    def test_pokmeon_initialization(self):
        test_generation = Generation('https://pokeapi.co/api/v2/', requests.Session(), 20)
        self.assertEqual(test_generation.base_url, 'https://pokeapi.co/api/v2/generation')
        self.assertIsInstance(test_generation.client, requests.Session)
        self.assertEqual(test_generation.page_limit, 20)

    def test_generation_get_info_by_id(self):
        test_generation = Generation('https://pokeapi.co/api/v2/', requests.Session(), 20)
        generation = test_generation.get_info(1)
        self.assertEqual(generation.name, 'generation-i')

    def test_generation_get_info_bulk(self):
        test_generation = Generation('https://pokeapi.co/api/v2/', requests.Session(), 20)
        generation_list = test_generation.get_info()
        self.assertEqual(len(generation_list), 9)

    def test_generation_get_info_bulk_small_page_limit(self):
        test_generation = Generation('https://pokeapi.co/api/v2/', requests.Session(), 5)
        generation_list = test_generation.get_info()
        self.assertEqual(len(generation_list), 9)