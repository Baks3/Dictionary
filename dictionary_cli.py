import argparse
import dictionary
import time

def main():
    parser = argparse.ArgumentParser(
        description="📚 Command-line Dictionary Tool"
    )
    
    parser.add_argument("command", choices=["define"], help="Command to run (currently only 'define')")
    parser.add_argument("word", help="The word to look up")

    parser.add_argument(
        "-f", "--file", default="data.json", help="Path to the JSON dictionary file"
    )

    args = parser.parse_args()

    data = dictionary.load_data(args.file)
    if data is None:
        print("❌ Failed to load dictionary data.")
        return

    print(f"🔍 Looking up: {args.word}")
    time.sleep(1)
    output = dictionary.translate(args.word, data)

    if isinstance(output, list):
        for item in output:
            print(f"👉 {item}")
    else:
        print(output)

if __name__ == "__main__":
    main()
