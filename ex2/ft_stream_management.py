import sys

if __name__ == "__main__":
    args = sys.argv
    if len(sys.argv) != 2:
        print(f"Usage: {args[0]} <file>\n")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{args[1]}'")
        text: str
        try:
            file = open(args[1], "r")
            print("---\n")
            text = file.read()
            print(text)
            print("---")
            file.close()
            print(f"File '{args[1]}' closed.")
            print("Transform data:\n")
            print("---\n")
            new_text = text.replace("\n", "#\n")
            print(new_text)
            print("---")
            print("Enter new file name (or empty): ", end="", flush=True)
            new_file_name = sys.stdin.readline().strip()
            if new_file_name == "":
                print("Not saving data.\n")
            else:
                try:
                    print(f"Saving data to '{new_file_name}'")
                    new_file = open(new_file_name, "w")
                    new_file.write(new_text)
                    new_file.close()
                    print(f"Data saved in file '{new_file_name}'.\n")
                except PermissionError as e:
                    print(
                        "[STDERR] Error opening/writing in file "
                        f"'{new_file_name}': {e}", file=sys.stderr)
                    print("Data not saved.\n")
        except Exception as e:
            print(
                f"[STDERR] Error opening file '{args[1]}': {e}\n",
                file=sys.stderr)
