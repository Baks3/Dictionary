import dictionary


def main():
    data = dictionary.load_data("data.json")

    while True:
        word = dictionary.get_user_input()
        if word is None:
            print("Exiting the program. Goodbye!")
            break
        output = dictionary.translate(word, data)

        if isinstance(output, list):
            for item in output:
                print(item)
        else:
            print(output)

if __name__ == "__main__":
    main()