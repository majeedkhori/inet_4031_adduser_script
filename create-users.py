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
    # loop through each line of input file via standard input
    for line in sys.stdin:
        
        # check if line starts with "#"    
        match = re.match("^#",line)

        # split line into different fields delimited with ":"
        fields = line.strip().split(':')

        # skip line if it starts with "#" (comment)  or doesn't have exactly 5 fields
        if match or len(fields) != 5:
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
        print(cmd)
        os.system(cmd)

        # print statement indicating password setup
        print("==> Setting the password for %s..." % (username))

        # command to set user password using echo and passwd
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        # print and execute command
        print(cmd)
        os.system(cmd)

        # loop through each group and assign user
        for group in groups:
            # skip if group is '-' (empty/no group)
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

# run main function
if __name__ == '__main__':
    main()
