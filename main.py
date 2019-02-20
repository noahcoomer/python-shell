### Noah Coomer & Jacob Hunt
### Operating Systems
### python-shell


import os
from os.path import expanduser
import datetime


def child_command(cmd, args):
    try:
        os.execvp("/usr/bin/" + cmd, args)
        os_exit(0)
    except:
        os_exit(1)

# Execute a user specififed command
def execute_command(command):
    pid = os.fork()
    # if we are the child process
    if pid == 0:
        # replace the memory space with the user specified command
        child_command(command[0], command[1:])
        
    
    
# Change the current working directory
def change_directory(current_directory, inp):
    new = os.path.join(current_directory, inp)
    if os.path.isdir(new):
        return(new)
    else: 
        print("\n No such directory \n")
        return(current_directory)
        

# Display a list of previously executed commands
def stat_command(history):
    for time, cmd in history:
        print(time, '    ', ' '.join(cmd))
       

# Display a list of all files and directories in the current working directory
def list_sources(current_directory):
    for file in os.listdir(current_directory):
        print(file)


def main():
    history = []

    # Set the current directory to "home" or equivalent
    current_directory = expanduser("~")
    while True:
        command = input(current_directory + "> ").split(' ')
        current_time = datetime.datetime.now().strftime("%H:%M")
        
        if command[0] == 'exit':
            print("Goodbye.")
            break

        elif command[0] == 'stat':
            stat_command(history)
            history.append((current_time, command))

        elif command[0] == 'ls':
            list_sources(current_directory)
            history.append((current_time, command))

        # change directory
        elif command[0] == 'cd':

            # cd will return the user to home if no directory is specified
            # the user will also be told if the directoey doesn't exist
            try:
                current_directory = change_directory(current_directory, command[1])
            except:
                if len(command) == 1:
                    current_directory = expanduser("~")
                else:
                    print("invalid format")
            history.append((current_time, command))

        else:
            #print("Sorry, I do not understand that command.")
            execute_command(command)
            history.append((current_time, command))
            

if '__main__' == __name__:
    main()
