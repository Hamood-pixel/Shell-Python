import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command = input()
        if command.startswith("echo "):
            print(command[5:])
        elif command.startswith("type "):
            if(command[5:]== "echo" or command[5:] == "exit" or command[5:] == "type"):
                print(f"{command[5:]} is a shell builtin")
            else:
                print(f"{command[5:]}: not found")
        elif command =="exit":
            break 
        else:
          print(f"{command}: command not found")
        pass


if __name__ == "__main__":
    main()
