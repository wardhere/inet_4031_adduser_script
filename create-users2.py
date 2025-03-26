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
             # Prompt the user to choose dry-run mode or normal execution
    dry_run_input = input("Run in dry-run mode? (Y/N): ").strip().lower()
    dry_run = dry_run_input == 'y'

    # Open the input file directly
    with open("create-users.input", "r") as f:
        for line_num, line in enumerate(f, start=1):
            # Check if the line is a comment
            match = re.match("^#", line)
            fields = line.strip().split(':')

            # Handle comment lines
            if match:
                if dry_run:
                    print(f"[Line {line_num}] Skipped (comment line): {line.strip()}")
                continue

            # Handle invalid lines
            if len(fields) != 5:
                if dry_run:
                    print(f"[Line {line_num}] ERROR: Invalid number of fields ({len(fields)} instead of 5): {line.strip()}")
                continue

            # Extract user information
            username = fields[0]
            password = fields[1]
            gecos = "%s %s,,," % (fields[3], fields[2])  # First Last
            groups = fields[4].split(',')

            # Creating the user
            print("==> Creating account for %s..." % username)
            cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
            if dry_run:
                print(f"[Dry Run] Would run: {cmd}")
            else:
                os.system(cmd)

            # Setting the password
            print(f"==> Setting the password for {username}...")
            cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
            if dry_run:
                print(f"[Dry Run] Would run: {cmd}")
            else:
                os.system(cmd)

            # Assign user to groups
            for group in groups:
                if group != '-':
                    print(f"==> Assigning {username} to the {group} group...")
                    cmd = f"/usr/sbin/adduser {username} {group}"
                    if dry_run:
                        print(f"[Dry Run] Would run: {cmd}")
                    else:
                        os.system(cmd)

if __name__ == '__main__':
    main()
