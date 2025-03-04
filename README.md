# Dictionary Application

## Overview
This is a simple **dictionary application** written in Python. It reads word definitions from a JSON file and allows users to search for words in a **case-insensitive** manner. The application provides the **definition** for the given word if it exists in the dictionary.

## Features
- Load word definitions from a JSON file.
- Case-insensitive word search (supports lowercase, uppercase, and title case).
- Continuous user input until the user chooses to exit.
- Error handling for missing files and invalid user input.

## Requirements
- Python 3.x
- A JSON file named `data.json` containing the word definitions.

## Installation
1. Ensure you have **Python 3** installed on your system. If not, download and install it from [python.org](https://www.python.org/).
2. Clone this repository or download the source code.
3. Place your JSON data file (`data.json`) in the same directory as the script.

## Usage
1. Run the script using the following command:
    ```sh
    python3 main.py
    ```
2. Enter the word you want to search for when prompted.
3. The application will display the **definition(s)** if the word exists in the dictionary.
4. To exit the application, type `exit` when prompted.

## Example JSON File
```json
{
    "python": ["A high-level programming language.", "A type of large snake."],
    "computer": ["An electronic device for storing and processing data."],
    "keyboard": ["An input device for typing text."]
}
```

## Example Output
```
Enter a word: python
Definitions:
1. A high-level programming language.
2. A type of large snake.

Enter a word: keyboard
Definitions:
1. An input device for typing text.

Enter a word: exit
Goodbye!
```

