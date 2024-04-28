import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        animals_data = json.load(handle)
    return animals_data


def generate_string(animals_data):
    """Receives animals data as parameter and returns a string containing the desired information"""
    output = ''
    for animal in animals_data:
        output += f'Name: {animal.get("name")}\n'
        output += f'Diet: {animal["characteristics"].get("diet")}\n'
        output += f'Location: {animal["locations"][0]}\n'
        output += f'Type: {animal["characteristics"].get("type")}\n'
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




def main():
    """Calls the functions in the program"""
    animals_data = load_data('animals_data.json')
    output = generate_string(animals_data)
    generate_html_file('animals_template.html',output)


if __name__ == "__main__":
    main()