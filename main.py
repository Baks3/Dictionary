import dictionary
import time


def main():
    data = dictionary.load_data("data.json")
    
    try: 
        while True:
            word = dictionary.get_user_input()
            if word is None:
                print("Exiting the program...")
                time.sleep(1)
                print("Goodbye!")
                break
            output = dictionary.translate(word, data)

            print("Fetching word...")
            time.sleep(1) 

            if isinstance(output, list):
                for item in output:
                    print(item)
            else:
                print(output)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()