import re
flag = 0
passwd = input ("Enter the password: ")
if not re.search('[0-9]', passwd):
    flag = 1

if not re.search('[a-z]', passwd):
    flag = 1

if not re.search('[A-Z]', passwd):
    flag = 1
    
if not re.search('[$@#!]', passwd):
    flag = 1

if len(passwd)<6:
    flag = 1
    
if (flag == 0):
    print ('Password is valid')
else:
    print ('Password is invalid')
