### Noah Coomer & Jacob Hunt
### Operating Systems
### python-shell


import os
from os.path import expanduser
import datetime


# Execute a child process
def child_command(cmd, args):
    try:
        os.execvp("/usr/bin/" + cmd, args)
        os._exit(0)
    except Exception as e:
        os._exit(1)
        print(e)

# Execute a user specified command
def execute_command(command):
    pid = os.fork()
    # if we have encountered an error
    if pid < 0:
        print("Fork failed.")
        return 1
    elif pid == 0:
        child_command(command[0], command)
    else:
        os.wait()
    
    
# Change the current working directory
def change_directory(current_directory, inp, directory_history):    
    if inp == '-':
        current_directory = directory_history[len(directory_history)-2]
        return current_directory

    elif inp == '.':
        return (current_directory)

    elif inp == '..': 
        split_directory = current_directory.split('/')
        split_directory = split_directory[:-1]
        return('/'.join(split_directory))

    else:   
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
    directory_history = []
    # Set the current directory to "home" or equivalent
    current_directory = expanduser("~")
    change_directory(current_directory, current_directory, [])
    while True:
        command = input(current_directory + "> ").split(' ')
        n = len(command) # this should only be 1 if we are using built-in functions except for cd
        current_time = datetime.datetime.now().strftime("%H:%M")

        # exit the terminal
        if command[0] == 'exit':
            print("Goodbye.")
            break

        # show terminal history
        elif command[0] == 'stat' and n == 1:
            stat_command(history)
            history.append((current_time, command))

        # list current sources
        elif command[0] == 'ls' and n == 1:
            list_sources(current_directory)
            history.append((current_time, command))

        # change directory
        elif command[0] == 'cd':

            # cd will return the user to home if no directory is specified
            # the user will also be told if the directoey doesn't exist
            try:
                current_directory = change_directory(current_directory, command[1], directory_history)
                directory_history.append(current_directory)
            except:
                if len(command) == 1:
                    current_directory = expanduser("~")
                else:
                    print("invalid format")

            history.append((current_time, command))

        # run a user specified command
        else:
            #print("Sorry, I do not understand that command.")
            execute_command(command)
            history.append((current_time, command))
            

if __name__ == '__main__':
    main()
