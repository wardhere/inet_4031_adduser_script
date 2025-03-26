#!/usr/bin/python3

# INET4031
# Abdinur Ward
# Date Created:03/25/25
# Date Last Modified:03/26/25

# Importing required modules:
import os      # Used to execute system-level shell commands
import re      # Used to perform regular expression matching
import sys     # Used to read from standard input (stdin)

def main():
    # Read each line from standard input (typically redirected from a file)
    for line in sys.stdin:

        # Skip lines that are comments (start with '#')
        match = re.match("^#", line)

        # Strip leading/trailing whitespace and split the line by colons
        fields = line.strip().split(':')

        # Skip this line if it's a comment or doesn't contain exactly 5 fields
        if match or len(fields) != 5:
            continue

        # Extract user information from the fields
        username = fields[0]
        password = fields[1]
        # Construct the GECOS field (used for full name/description)
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Extract group names, split by commas (can be multiple groups)
        groups = fields[4].split(',')

        # Inform the user account is being created
        print("==> Creating account for %s..." % username)
        # Prepare the adduser command with GECOS info and no initial password
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        #print(cmd)
        os.system(cmd)

        # Inform that the password is being set for the user
        print("==> Setting the password for %s..." % username)
        # Prepare the command to set the user's password using sudo and passwd
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        #print(cmd)
        os.system(cmd)

        # Loop through each group and assign the user if not a placeholder '-'
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                #print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()

