import os
import sys
from datetime import datetime


def main() -> None:
    file_name = ""
    final_path = ""

    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        file_name = sys.argv[f_index + 1]
        final_path = file_name
        print("Found file: ", file_name)

    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        if "-f" in sys.argv and sys.argv.index("-f") > d_index:
            f_index = sys.argv.index("-f")
            folders = sys.argv[d_index + 1: f_index]
            print("Folders: ", folders)
        else:
            folders = sys.argv[d_index + 1:]
            print("Folders: ", folders)
        folder_path = os.path.join(*folders)
        os.makedirs(folder_path, exist_ok=True)
        if "-f" in sys.argv:
            final_path = os.path.join(folder_path, file_name)

    if final_path:
        content_lines = []
        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            content_lines.append(user_input)
        with open(final_path, "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp}\n")
            for i, content in enumerate(content_lines, start=1):
                file.write(f"{i} {content}\n")


if __name__ == "__main__":
    main()
