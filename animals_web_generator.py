import json

def load_data(file_path):
    """" Loads a JSON file and returns a dictionary of data """
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        return data

def load_html(file_path):
    """" Loads a HTML file and returns a string of data """
    with open(file_path, "r") as html_file:
        data = html_file.read()
        return data

def write_animals_html(html_data, new_file_path, str_replace, data):
    """Replaces a given html string with data and stores the html under a new file."""

    new_data = html_data.replace(str_replace, data)
    print(new_data)
    try:
        with open(new_file_path, "w") as new_file:
            new_file.write(new_data)
        print("Successfully wrote new file")
    except:
        print("Error writing to file")


def show_animal(animal_data):
    """ Prints an overview of some of the animal data if it exists otherwise it just prints nothing.
    Data will be printed in the following format:
        Name: American Foxhound
        Diet: Omnivore
        Location: North-America
        Type: Hound
        \n
    """
    data = "" #initialize data
    for animal in animal_data:

        if "name" in animal:
            name = animal["name"]
            data += f"Name: {name}" + "\n"
        if "characteristics" in animal:
            if "diet" in animal["characteristics"]:
                diet = animal["characteristics"]["diet"]
                data += f"Diet: {diet}" + "\n"
        if "locations" in animal:
            location = animal["locations"][0]
            data += f"Location: {location}" + "\n"
        if "characteristics" in animal:
            if "type" in animal["characteristics"]:
                type = animal["characteristics"]["type"]
                data += f"Type: {type}" + "\n"
        data += "\n"
    return data

def main():
    animals_data = load_data('animals_data.json')
    data = show_animal(animals_data)
    html_data = load_html('animals_template.html')
    write_animals_html(html_data=html_data, new_file_path='animals.html', str_replace='__REPLACE_ANIMALS_INFO__', data=data)

main()

