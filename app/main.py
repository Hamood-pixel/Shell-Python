import sys
import os


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command = input()
        if command.startswith("echo "):
            print(command[5:])
        elif command.startswith("type "):
            if(command[5:]== "echo" or command[5:] == "exit" or command[5:] == "type"):
                print(f"{command[5:]} is a shell builtin") #if the type command receives a valid builtin command, it will print that command
            else:
                #if the type command is not a shell builtin, then it will check the path directories for a file and match 
                found = False
                for path in os.environ["PATH"].split(os.pathsep):
                    full_path = os.path.join(path, command[5:])
                    if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                        print(f"{command[5:]} is {full_path}")
                        found = True
                        break
                if found == False:
                  print(f"{command[5:]}: not found")
        elif command =="exit":
            break 
        else:
          print(f"{command}: command not found")
        pass


if __name__ == "__main__":
    main()
