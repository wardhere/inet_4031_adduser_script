### INET4031 Add Users Script and User List

## Program Description

This program automates the process of adding multiple users to a Linux system, saving time and reducing human error. Normally, a system administrator would use several commands such as adduser, passwd, and adduser <user> <group> to create user accounts, set passwords, and assign users to groups manually. Doing this for multiple users is tedious and error-prone.
This Python script simplifies that task by reading a list of users from an input file and executing the necessary Linux commands to create each user, assign them a password, and add them to one or more groups. It mirrors the manual process by using the exact same Linux commands internally but does so in an automated and efficient way.

## Program User Operation

To operate the program, the user simply runs the Python script and is prompted whether they want to run it in "dry-run" mode or execute the actual user creation process. The script reads a file containing user data, processes each line, and either simulates or executes the necessary system commands. If errors or malformed lines are detected, they are reported in dry-run mode.

## Input File Format

Each line in the input file represents a single user and must contain exactly five fields, separated by colons (:):
username: password:LastName : FirstName:group1,group2
username: the new user's login name
password: the password to be set for the user
LastName: the user's last name (used in the GECOS field)
FirstName: the user's first name (used in the GECOS field)
group1,group2: a comma-separated list of groups the user should be added to
To skip a line, the user should prefix it with a #, which the script recognizes as a comment.
To exclude a user from any groups, the user can use a dash (-) in place of the group list:
username: password: LastName: FirstName:-

## Command Execution

To run the program, use the following command in the terminal:
./create-users.py < create-users.input
If the script is not executable, make it so with:
chmod +x create-users.py
Alternatively, you can run it directly with Python:
python3 create-users.py < create-users.input

## "Dry Run"

When prompted at the start of the script, typing Y enables "dry-run" mode. In this mode:
No system commands are actually executed.
Instead, the script prints the commands that would be run. It displays messages about skipped comment lines and lines with invalid field counts.
This is useful for verifying the input file before making real changes to the system.
Typing N executes the script in normal mode, performing the actual user creation, password setting, and group assignments.
