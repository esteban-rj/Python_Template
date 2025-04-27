from django.test import TestCase, Client
from django.urls import reverse
import json
import requests_mock

class PokemonAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('get_pokemon')

    def test_get_pokemon_ditto(self):
        #mock call to the pokemon api
        with requests_mock.Mocker() as m:
            m.get('https://pokeapi.co/api/v2/pokemon/ditto', json={'abilities': [{'ability': {'name': 'limber'}}]})
            # Make a GET request with name=ditto
            response = self.client.get(f'{self.url}?name=ditto')
            
            # Check if the response status code is 200
            self.assertEqual(response.status_code, 200)
            
            # Parse the JSON response
            data = json.loads(response.content)
            
            # Check if the response contains the expected structure
            self.assertIn('abilities', data)
            self.assertIsInstance(data['abilities'], list)
            
            # Check if Ditto has at least one ability
            self.assertGreater(len(data['abilities']), 0)
            
            # Check if the first ability has the expected structure
            first_ability = data['abilities'][0]
            self.assertIn('ability', first_ability)
            self.assertIn('name', first_ability['ability'])
            
            # Verify it's Ditto's ability (limber)
            self.assertEqual(first_ability['ability']['name'], 'limber')
