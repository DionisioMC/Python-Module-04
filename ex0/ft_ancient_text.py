import sys
import typing

if __name__ == "__main__":
    args = sys.argv
    if len(sys.argv) != 2:
        print(f"Usage: {args[0]} <file>\n")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{args[1]}'")
        try:
            file = open(args[1], "r")
            print("---\n")
            print(file.read())
            print("---")
            file.close()
            print(f"File '{args[1]}' closed.")
        except Exception as e:
            print(f"Error opening file '{args[1]}': {e}\n")
