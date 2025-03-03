# Translation Dictionary

## Overview
This is a simple translation dictionary application written in Python. It reads translations from a JSON file and allows users to search for words in a case-insensitive manner. The application provides the translation for the given word if it exists in the dictionary.

## Features
- Load translation data from a JSON file.
- Case-insensitive word search (supports lowercase, uppercase, and title case).
- Continuous user input until the user chooses to exit.
- Error handling for file operations and invalid user input.

## Requirements
- Python 3.x
- A JSON file named `data.json` containing the translation data.

## Installation
1. Ensure you have Python 3 installed on your system. If not, download and install it from [python.org](https://www.python.org/).
2. Clone this repository or download the source code.
3. Place your JSON data file (`data.json`) in the same directory as the script.

## Usage
1. Run the script using the following command:
    ```sh
    python translate.py
    ```
2. Enter the word you want to search for when prompted.
3. The application will display the translation if the word exists in the dictionary.
4. To exit the application, type `exit` when prompted for input.

## Example
```json
{
    "hello": ["hola", "bonjour", "hallo"],
    "world": ["mundo", "monde", "welt"],
    "python": ["pitón", "python", "python"]
}
