### Noah Coomer & Jacob Hunt
### Operating Systems
### python-shell


import os
from os.path import expanduser
import datetime


# Execute a user specified command
def execute_command(command):
    pid = os.fork()
    # if we have encountered an error
    if pid < 0:
        print("Fork failed.")
        return 1
    elif pid == 0:
        try:
            os.execvp("/usr/bin/" + command[0], command)
            os._exit(0)
        except Exception as e:
            # if we can't find the program in /usr/bin/ check /bin/
            if e.errno == 2:
                try:
                    os.execvp("/bin/" + command[0], command)
                    os._exit(0)
                except Exception as e:
                    print(e)
                    os._exit(1)
            else:
                print(e)
                os._exit(1)
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


def main():
    history = []
    directory_history = []
    
    # Set the current directory to "home" or equivalent
    os.chdir(expanduser("~"))

    while True:
        command = input(os.getcwd() + "> ").split(' ')
        n = len(command)
        current_time = datetime.datetime.now().strftime("%H:%M")

        # exit the terminal
        if command[0] == 'exit':
            print("Goodbye.")
            break

        elif command[0] == '':
            continue

        # show terminal history
        elif command[0] == 'stat' and n == 1:
            stat_command(history)
            history.append((current_time, command))


        # change directory
        elif command[0] == 'cd':

            # cd will return the user to home if no directory is specified
            # the user will also be told if the directory doesn't exist
            try:
                current_directory = change_directory(os.getcwd(), command[1], directory_history)
                directory_history.append(current_directory)
                os.chdir(current_directory)

            except:
                if len(command) == 1:
                    os.chdir(expanduser("~"))
                else:
                    print("invalid format")

            history.append((current_time, command))

        # run a user specified command
        else:
            execute_command(command)
            history.append((current_time, command))
            

if __name__ == '__main__':
    main()
