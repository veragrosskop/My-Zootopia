import json

def load_data(file_path):
    """" Loads a JSON file and returns a dictionary of data """
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        return data

def show_animal(data):
    for animal in data:

        if "name" in animal:
            name = animal["name"]
            print(f"Name: {name}")
        if "characteristics" in animal:
            if "diet" in animal["characteristics"]:
                diet = animal["characteristics"]["diet"]
                print(f"Diet: {diet}")
        if "locations" in animal:
            location = animal["locations"][0]
            print(f"Location: {location}")
        if "characteristics" in animal:
            if "type" in animal["characteristics"]:
                type = animal["characteristics"]["type"]
                print(f"Type: {type}")
        print("")

def main():
    animals_data = load_data('animals_data.json')
    show_animal(animals_data)

main()

