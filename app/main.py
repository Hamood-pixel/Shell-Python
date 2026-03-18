import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    command = input()
    print(f"{command} : not found")
    pass


if __name__ == "__main__":
    main()
