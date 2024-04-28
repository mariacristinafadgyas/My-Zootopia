import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        animals_data = json.load(handle)
    return animals_data


def access_animal_data(animals_data):
    """Displays the animal data"""
    for animal in animals_data:
        print(f'Name: {animal.get("name")}')
        print(f'Diet: {animal["characteristics"].get("diet")}')
        print(f'Location: {animal["locations"][0]}')
        if animal["characteristics"].get("type") is None:
            print()
        else:
            print(f'Type: {animal["characteristics"].get("type")}')
        print()


def main():
    """Calls the functions in the program"""
    animals_data = load_data('animals_data.json')
    access_animal_data(animals_data)



if __name__ == "__main__":
    main()