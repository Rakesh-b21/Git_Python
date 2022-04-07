import re
print("""For a password to be valid:\n1.It should atleast one lowercase and one uppercase letter
2.It should contain atleast one number
3.It should also contain atleast one of these characters [@,$,#]
4.The length of the password should be greater than 5 and less than 13
Enter the list of password and check if they are valid or not: """)
passwords = input().split()
for i in passwords:
    if 5<len(i)<13:
        if re.search("[a-z]",i) and re.search("[A-Z]",i) and re.search("[$#@]",i):
            print("valid password: ",i)
        else:print("Invalid password: ",i)
    else: print("Invalid length, password should be between 6 and 12 characters")