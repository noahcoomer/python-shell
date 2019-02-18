### Noah Coomer & Jacob Hunt
### Operating Systems
### python-shell

import os
import datetime


# Change the current working directory
def change_directory():
    print()


# Display a list of previously executed commands
def stat_command(history):
    for time, cmd in history:
        print(time, '    ', cmd)
       

# Display a list of all files and directories in the current working directory
def list_sources():
    print()


def main():
    history = []
    while True:
        command = input("$ ")
        current_time = datetime.datetime.now().strftime("%H:%M")
        
        if command == 'exit':
            print("Goodbye.")
            break
        elif command == 'stat':
            stat_command(history)
            history.append((current_time, command))
        elif command == 'ls':
            list_sources()
            history.append((current_time, command))
        elif command == 'cd':
            change_directory()
            history.append((current_time, command))
        else:
            print("Sorry, I do not understand that command.")

main()
