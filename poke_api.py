'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests
import image_lib
import os
 
POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'
 
def main():
    # Test out the get_pokemon_into() function
    # Use breakpoints to view returned dictionary
    #poke_info = get_pokemon_info("Rockruff")
    #poke_info = get_pokemon_info(123)
    download_pokemon_image('ditto', r'D:\clg')
    return
 
def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.
 
    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)
 
    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # Clean the Pokemon name parameter by:
    # - Converting to a string object, 
    # - Removing leading and trailing whitespace, and
    # - Converting to all lowercase letters
    pokemon_name = str(pokemon_name).strip().lower()
 
    # Build the clean URL for the GET request
    url = POKE_API_URL + pokemon_name
 
    # Send GET request for Pokemon info
    print(f'Getting information for {pokemon_name}...', end='')
    response_msg = requests.get(url)
 
    # Check if request was successful
    if response_msg.status_code == requests.codes.ok:
        print('success')
        # Return dictionary of Pokemon info
        return response_msg.json()
    else:
        print('failure')
        print(f'Response code: {response_msg.status_code} ({response_msg.reason})')         
        return
 
def get_pokemon_names_list(offset=0, limit=100000):
    query_str_params = {
        'offset' :offset,
        'limit' :limit
    }

    response_msg = requests.get(POKE_API_URL, params=query_str_params)

    if response_msg.status_code == requests.codes.ok:
        pokemon_dict = response_msg.json()
        pokemon_names_list = [p['name'] for p in pokemon_dict['results']]
        return pokemon_names_list
    else:
        print('failure')
        print(f'Response code: {response_msg.status_code} ({response_msg.reason})')
        return
    
def download_pokemon_image(pokemon_name, save_directory):
    pokemon_details = get_pokemon_details(pokemon_name)
    if pokemon_details is None:
        return
    
    img_url = pokemon_details['sprites']['other']['official-artwork']['front_default']

    image_bytes = image_lib.download_image(img_url)
    if image_bytes is None:
        return
    
    file_extn =  img_url.split('.')[-1]
    image_path = os.path.join(save_directory, pokemon_name)
    
    if image_lib.save_image_file(image_bytes, image_path):
        return image_path

    return

if __name__ == '__main__':
    main()