import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        animals_data = json.load(handle)
    return animals_data


def serialize_animal(animal_obj):
    """Receives an animal object as parameter and returns a string containing
    the desired data for a single animal"""
    output = ''
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal_obj.get("name")}</div>'
    output += '<p class="card__text">'
    output += '<ul class ="animal_data">'
    output += f'<li><strong>Location: </strong>{animal_obj["locations"][0]}</li>\n'
    output += f'<li><strong>Type: </strong>{animal_obj["characteristics"].get("type")}<li>\n'
    output += f'<li><strong>Diet: </strong>{animal_obj["characteristics"].get("diet")}<li>\n'
    output += f'<li><strong>Scientific name: </strong>{animal_obj["taxonomy"].get("scientific_name")}<li>\n'
    output += f'<li><strong>Color: </strong>{animal_obj["characteristics"].get("color")}<li>\n'
    output += f'<li><strong>Lifespan: </strong>{animal_obj["characteristics"].get("lifespan")}<li>\n'
    output += '</ul>\n'
    output += '</p>\n'
    output += '</li>'
    return output


def serialize_animals(animals_data):
    """Receives the list animals_data as parameter and returns a string containing
       the desired data for the whole list of animals"""
    output = ''
    output += f'<div class="skin__type"><strong>Skin type: </strong>{animals_data[0]["characteristics"].get("skin_type")}</div>'
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


def generate_html_file(html_path, output):
    """Receives the output string of the previous function and the path of the HTML
    template as parameters and writes the updated HTML file"""
    with open(html_path, "r") as fileobj:
        template = fileobj.read()
    if "__REPLACE_ANIMALS_INFO__" in template:
        replaced_output = template.replace("__REPLACE_ANIMALS_INFO__", output)
    with open("animals.html", "w") as file_output:
        file_output.write(replaced_output)
    print("\u001b[36mThe HTML file was generated.\u001b[0m")

def user_selection():
    """Asks the user to select the type of skin for the animal"""
    while True:
        user_input = input("""\u001b[35mSkin types:
Hair
Fur
Scales
Please select a skin type: \u001b[0m
""")
        if user_input.lower() == "hair" or user_input.lower() == "fur" or user_input.lower() == "scales":
            return user_input
        elif user_input.lower() == "quit":
            quit()
        else:
            print("\u001b[31mPlease select one of the options: hair, fur, scales or quit(to quit).\u001b[0m")


def generate_html_user_selection(animals_data, user_input):
    """Receives the user input and the animal data as parameters and returns a list of
    dictionaries containing the animals based on the user selection"""
    animals_data_user_choice = []
    for animal in animals_data:
        if user_input.lower() == "hair" and animal['characteristics']['skin_type'] == "Hair":
            animals_data_user_choice.append(animal)
        elif user_input.lower() == "fur" and animal['characteristics'].get('skin_type') == "Fur":
            animals_data_user_choice.append(animal)
        elif user_input.lower() == "scales" and animal['characteristics'].get('skin_type') == "Scales":
             animals_data_user_choice.append(animal)
    return animals_data_user_choice


def main():
    """Calls the functions in the program"""
    animals_data = load_data('animals_data.json')
    user_input = user_selection()
    animals_data_user_choice = generate_html_user_selection(animals_data, user_input)
    output = serialize_animals(animals_data_user_choice)
    generate_html_file('animals_template.html', output)


if __name__ == "__main__":
    main()