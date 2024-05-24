import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def user_animal_selection():
    """Asks user for animal selection"""
    user_input = input("\u001b[31mEnter a name of an animal: \u001b[0m")
    return user_input


def get_data(animal_name):
    """Fetches animals data from the free ninja API"""
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        animals_data = response.json()
        return animals_data
    else:
        print("Error:", response.status_code, response.json())


def main():
    """Calls the functions that are responsible for retrieving data"""
    animal_name = user_animal_selection()
    get_data(animal_name)


if __name__ == "__main__":
    main()