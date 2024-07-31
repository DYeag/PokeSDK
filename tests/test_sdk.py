from unittest import TestCase
from src.pokesdk.sdk import PokeSDK
from src.pokesdk.pokemon import Pokemon
from src.pokesdk.generation import Generation
import requests


class TestSDK(TestCase):
    def test_sdk_initialization_default(self):
        test_sdk = PokeSDK()
        self.assertIsInstance(test_sdk.client, requests.Session)
        self.assertEqual(test_sdk.page_limit, 20)
        self.assertIsInstance(test_sdk.pokemon, Pokemon)
        self.assertIsInstance(test_sdk.generation, Generation)

    def test_sdk_initialization_page_limit(self):
        test_sdk = PokeSDK(100)
        self.assertIsInstance(test_sdk.client, requests.Session)
        self.assertEqual(test_sdk.page_limit, 100)
        self.assertIsInstance(test_sdk.pokemon, Pokemon)
        self.assertIsInstance(test_sdk.generation, Generation)
