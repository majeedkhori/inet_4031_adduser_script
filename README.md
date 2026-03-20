# inet_4031_adduser_script

## Program Description
This program is a Python script that automates the process of creating user accounts on a Linux system. Normally, a system administrator would manually create users with commands like "adduser", set passwords using the "passwd" command, and assign users to groups with more "adduser" commands. This process is repetitive and takes too long when dealing with many users, so automation is a great idea.

## Program User Operation
This program works by reading an input file (line by line) that contains user information and processing each line to create users, set passwords, and assign group memberships. The user provides the input file and runs the script, and the script handles the rest automatically.

### Input File Format
Each line in the input file should follow this format:

username:password:last:first:groups

- username: user's username
- password: user's password
- last: user's last name
- first: user's first name
- groups: comma separated list of groups to add the user to

Other:
- Comments/lines starting with "#" are skipped by the program.
- Lines that don't have exactly 5 fields are also skipped.
- A "-" symbol in the groups field means the user isn't added to any groups.

### Command Execution
Run the script using:

./create-users.py < create-users.input

The script will execute system commands including "adduser" and "passwd" with the "os.system()" function.

### "Dry Run"
A dry run allows the script to be tested without actually creating users or modifying the system. In this mode, the script prints the commands that would be executed instead of running them. This allows the user to verify that the input file and commands are correct before running the script normally. This can save headaches moving forward.
