from sdk import PokeSDK


client = PokeSDK()

print(client.pokemon.get_info('charmander'))