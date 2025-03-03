import json

with open("data.json") as file:
    data = json.load(file)

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "Word cannot be found!"



word = input("Enter the word you want to search: ")
output = translate(word)
if isinstance(output, list):
    for item in output:
        print(item)
else:
    print(output)
