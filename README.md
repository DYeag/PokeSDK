# Poke SDK

## SDK Installation

```bash
pip install git+https://github.com/DYeag/PokeSDK.git
```

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

Below you can see the sample of importing, instantiating, and making some API calls.
It is worth noting that the PokeSDK class can accept a integer page_limit parameter, to change the default pagination fro the PokeAPI.
I believe the default limit is 20 for the PokeAPI, but can be overridden.

```python
from pokesdk import PokeSDK

s = PokeSDK()

bulbasaur = s.pokemon.get_info('bulbasaur')
bulbasaur_also = s.pokemon.get_info(1)
pokemon_list = s.pokemon.get_info()

gen_1 = s.generation.get_info('generation-i')
gen_1_also = s.generation.get_info(1)
generation_list = s.generation.get_info()

```

### Getting Pokemon

Using the pokemon.get_info method, you can query a list of all pokemon or a specific pokemon by name or id.
The returned object will be a custom python object created from the PokeAPI response json, allowing you to access some of the info as properties.

```python
from pokesdk import PokeSDK

s = PokeSDK()

bulbasaur = s.pokemon.get_info(1)
print(bulbasaur.name)   # bulbasaur
print(bulbasaur.height) # 7
print(bulbasaur.weight) # 69

pokemon_list = s.pokemon.get_info()

```

### Getting Generations

Using the generation.get_info method, you can query a list of all generations or a specific generation by name or id.
The returned object will be a custom python object created from the PokeAPI response json, allowing you to access some of the info as properties.

```python
from pokesdk import PokeSDK

s = PokeSDK()

gen_1 = s.generation.get_info(1)
print(gen_1.id)     # 1
print(gen_1.name)   # generation-i

generation_list = s.generation.get_info()

```

### Testing

I've added in some unit tests, these incorporate some real API calls with some assert verification on the Responses.
The tests can be viewed in the tests directory and can be run with the following command:
```bash
python -m unittest discover
```

### Design Decisions

#### Class Structure
I separated the main potions of the SDK into 4 classes.
1. The SDK class
2. The Pokemon class
3. The Generation class
4. The GenericResource class
This was done so that related portions of the SDK can be handled per file for organization and cleanliness.

#####The SDK Class
This class is the one users will initialize, and will handle the initialization of the underlying Pokemon and Generation objects.
This class creates and configures the requests session for the underlying objects to use for making API calls as well as holds some generic information such as the base_url for the PokeAPI and the page_limit.
It is done this way to make it easy for users to create/interact with the object. Also to keep the session creation/configuration in one place so the effort is not duplicated later.

#####The Pokemon Class
This class is for interacting with the pokemon API endpoints: https://pokeapi.co/api/v2/pokemon/
I've simplified the usage by having only a single method on the class that gives a list of pokemon or a specific one based on the input paramter, id, name or empty.

#####The Generation Class
This class is for interacting with the generation API endpoints: https://pokeapi.co/api/v2/generation/
I've simplified the usage by having only a single method on the class that gives a list of generations or a specific one based on the input paramter, id, name or empty.

#####The GenericResource Class
This class simply creates a custom python object based on the dictionaries returned by the PokeAPI.
Simplifies usage by allowing users to access info as properties instead of needing to access everything through a dictionary.
```python
from pokesdk import PokeSDK

s = PokeSDK()

bulbasaur = s.pokemon.get_info(1)

print(bulbasaur.name)    # We can get the name like this

print(bulbasaur["name"]) # Instead of like this

```

####Pagination
The requirements doc mentioned pagination. I saw that the pagination was limited at 20 by default with the PokeAPI, so i have kept that as the default.
However users can intialize the PokeSDK with an integer input that changes the page limit to that number. This can be seen with both the pokemon and generation get_info methods.
The underlying hadling of the pagination is within the common.py file, you will see a get_request and a get_paged_request depending on whether the API call being made is for multiple pokemon/generations or a single.

####Python modules used
I tried to use mostly default python modules, i did use the standard python requests module for the API calls.
And other than that, just the unittest module for the tests that reach out and verify API responses.

####Retries
As this API is fairly simple, not requiring authentication. I did add retries to the PokeSDK class in sdk.py.
This was more to show that this PokeSDK class is where the API session object would be configured, and it would make more sense for something like authentication.
Since i believe the requests module already has builtin retries.


<!-- End SDK Example Usage [usage] -->
