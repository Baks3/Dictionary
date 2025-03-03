import json

def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON.")
        return None

def translate(word, data):
    if data is None:
        return "Error: Data could not be loaded."
        
    if word.lower() in data:
        return data[word.lower()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    else:
        return "Word cannot be found!"

data = load_data("data.json")

word = input("Enter the word you want to search: ").strip()

if not word:
    print("Error: No word entered. Please try again.")
else:
    output = translate(word, data)

    if isinstance(output, list):
        for item in output:
            print(item)
    else:
        print(output)
