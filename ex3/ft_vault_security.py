def secure_archive(file_name: str, action: str = "r", to_write: str = "") -> tuple[bool, str]:
    if action in ["r", "w"]:
        try:
            content: str
            with open(file_name, action) as file:
                if action == "r":
                    content = file.read()
                else:
                    file.write(to_write)
                    content = to_write
            return (True, content)
        except Exception as e:
            return (False, str(e))
    else:
        print("The provided action isn't supported")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file")
    result = secure_archive("foo")
    print(f"{result}\n")
    print("Using 'secure_archive' to read from an inaccessible file:")
    result = secure_archive("ex3/etc/master.passwd")
    print(f"{result}\n")
    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ex3/ancient_fragments.txt")
    print(f"{result}\n")
    print("Using 'secure_archive' to write previous content to a new file:")
    result = secure_archive("ex3/new_fragment.txt", "w",
                            "Content successfully written to file")
    print(f"{result}\n")
