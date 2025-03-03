import json

def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            data = {key.lower(): value for key, value in data.items()}
        return data
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON.")
        return None

def get_user_input():
    while True:
        word = input("Enter the word you want to search (or type 'exit' to quit): ").strip()
        if word.lower() == 'exit':
            return None
        elif not word:
            print("Error: No word entered. Please try again.")
        else:
            return word

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