import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command = input()
        print(f"{command}: command not found")
        if command == "exit":
            break #Exit the shell/loop when the user types exit 
        pass


if __name__ == "__main__":
    main()
