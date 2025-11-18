# cli.py
import argparse
import json
from .parser import parse_user_prompt

def main():
    parser = argparse.ArgumentParser(description="NLU Parser CLI")
    parser.add_argument("text", nargs="?", help="Text to parse")
    parser.add_argument("--file", "-f", help="Path to input text file")

    args = parser.parse_args()
    if args.file:
        with open(args.file, "r") as fh:
            text = fh.read()
    elif args.text:
        text = args.text
    else:
        print("Provide text or --file input")
        return

    result = parse_user_prompt(text)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
