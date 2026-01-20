# Main run file. Holds User interface

from creator import *

def main():
    print("Hello User do you want create a character?")
    choice = input("1 to create")
    if choice == '1':
        makeChar()

main()