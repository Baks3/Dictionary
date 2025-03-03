import dictionary


def main():
    data = dictionary.load_data("data.json")

    word = input("Enter the word you want to search: ").strip()

    if not word:
        print("Error: No word entered. Please try again.")
    else:
        output = dictionary.translate(word, data)

        if isinstance(output, list):
            for item in output:
                print(item)
        else:
            print(output)


if __name__ == "__main__":
    main()