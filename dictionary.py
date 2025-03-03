import json
from difflib import get_close_matches

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
    exit_commands = ['exit', 'quit', 'q']  

    while True:
        word = input("Enter the word you want to search (or type 'exit', 'quit', or 'q' to quit): ").strip()

        if not word:
            print("⚠️ Error: No word entered. Please try again.")
            continue  
        
        if word.lower() in exit_commands:
            return None  
        
        return word  


def translate(word, data):
    if data is None:
        return "Error: Data could not be loaded."

    word_lower = word.lower()
    if word_lower in data:
        return data[word_lower]
    
    matches = get_close_matches(word_lower, data.keys(), n=3, cutoff=0.7)
    if matches:
        return f"Word cannot be found! Did you mean: {', '.join(matches)}?"
        
    return "Word cannot be found!"