#!/usr/bin/python3

# INET4031
# Majeed Khori
# Date Created: 3/19/26
# Date Last Modified: 3/1926

# import statements:
# os - Access Linux OS and system components
# re - regular expression module, used for pattern matching
# sys - system module, used for standard input
import os
import re
import sys

# main function

def main():
    # ask user if they want to do a dry run, store as boolean
    # dry run skips commands and just prints out what would happen later on
    dry_run_input = input("Do you want to do a dry run? (Y/N): ").strip().upper()
    dry_run = True if dry_run_input == "Y" else False

    # loop through each line of input file via standard input
    for line in sys.stdin:
        
        # check if line starts with "#"    
        match = re.match("^#",line)

        # split line into different fields delimited with ":"
        fields = line.strip().split(':')

        # skip line if it starts with "#" (comment)  or doesn't have exactly 5 fields
        if match or len(fields) != 5:
            if dry_run:
                if match:
                    print("skipped comment")
                else:
                    print("skipped line, not 5 fields")
            continue

        # extract username and password from input file, create gecos field to stor user info in /etc/passwd
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # split the groups field into a comma separated list
        groups = fields[4].split(',')

        # print statement indicating user creation
        print("==> Creating account for %s..." % (username))

        # command to create user accounts, start with no password
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        # print and execute command
        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        # print statement indicating password setup
        print("==> Setting the password for %s..." % (username))

        # command to set user password using echo and passwd
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        # print and execute command
        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        # loop through each group and assign user
        for group in groups:
            # skip if group is '-' (empty/no group)
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                if dry_run:
                    print(cmd)
                else:
                    os.system(cmd)

# run main function
if __name__ == '__main__':
    main()
