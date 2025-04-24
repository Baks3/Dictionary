import json
from difflib import get_close_matches

def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            data = {key.lower(): value for key, value in data.items()}
        return data
    except FileNotFoundError:
        print("❌ Error: The file was not found.")
        return None
    except json.JSONDecodeError:
        print("❌ Error: The file is not a valid JSON.")
        return None

def get_user_input():
    exit_commands = ['exit', 'quit', 'q']  

    while True:
        word = input("\n📖 Enter the word you want to search (or type 'exit', 'quit', or 'q' to quit): ").strip()

        if not word:
            print("⚠️ Error: No word entered. Please try again.")
            continue  
        
        if word.lower() in exit_commands:
            return None  
        
        return word  

def translate(word, data):
    if data is None:
        return "❌ Error: Data could not be loaded."

    word_lower = word.lower()
    if word_lower in data:
        return format_output(word_lower, data[word_lower])
    
    # Fuzzy matching suggestions
    matches = get_close_matches(word_lower, data.keys(), n=3, cutoff=0.7)
    if matches:
        print(f"❓ Word not found. Did you mean:")
        for i, match in enumerate(matches, 1):
            print(f"{i}. {match}")
        
        choice = input("➡️ Enter the number of the correct word, or press Enter to skip: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(matches):
            chosen_word = matches[int(choice) - 1]
            return format_output(chosen_word, data[chosen_word])
        return "❌ Word not found. No match selected."
        
    return "❌ Word cannot be found!"

def format_output(word, entry):
    output = f"\n📘 Word: {word}"

    # If the value is a list of strings (multiple meanings)
    if isinstance(entry, list):
        output += "\n📖 Definitions:"
        for i, meaning in enumerate(entry, 1):
            output += f"\n  {i}. {meaning}"
        return output
    
    # If the entry is a dictionary with more structured data
    if isinstance(entry, dict):
        definition = entry.get("definition", "No definition found.")
        synonyms = entry.get("synonyms", [])
        example = entry.get("example", "")
        
        output += f"\n📖 Definition: {definition}"
        if synonyms:
            output += f"\n🟰 Synonyms: {', '.join(synonyms)}"
        if example:
            output += f"\n💬 Example: {example}"
        return output

    # Fallback for basic string
    return output + f"\n📖 Definition: {entry}"
