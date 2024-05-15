import requests


def user_animal_selection():
    """Asks user for animal selection"""
    user_input = input("\u001b[31mEnter a name of an animal: \u001b[0m")
    return user_input


def get_data(animal_name):
    """Fetches animals data from the free ninja API"""
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    response = requests.get(api_url, headers={'X-Api-Key': '8CFm02DRZSY8gOcb8OIFog==tLAauWRZOqShOiBQ'})
    if response.status_code == requests.codes.ok:
        animals_data = response.json()
        return animals_data
    else:
        print("Error:", response.status_code, response.json())


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


def serialize_animals(animals_data, animal_name):
    """Receives the list animals_data as parameter and returns a string containing
       the desired data for the whole list of animals"""
    output = ''
    if animals_data == []:
        output += f'<h2>The animal <em>{animal_name}</em> does not exist in the database.</h2>\n'
    else:
        for animal in animals_data:
            output += serialize_animal(animal)
    return output


def generate_html_file(html_path, output):
    """Receives the output string of the previous function and the path of the HTML
    template as parameters and generates the HTML file"""
    with open(html_path, "r") as fileobj:
        template = fileobj.read()
    if "__REPLACE_ANIMALS_INFO__" in template:
        replaced_output = template.replace("__REPLACE_ANIMALS_INFO__", output)
    with open("animals.html", "w") as file_output:
        file_output.write(replaced_output)
    print("\u001b[36mWebsite was successfully generated to the animals.html file.\u001b[0m")


def main():
    """Calls the functions in the program"""
    animal_name = user_animal_selection()
    animals_data = get_data(animal_name)
    output = serialize_animals(animals_data, animal_name)
    generate_html_file('animals_template.html', output)


if __name__ == "__main__":
    main()