import string

password = input("Enter password: ")
upper=False
lower=False
digit=False
special=False
length=len(password)>=5

for char in password:
    if char in string.ascii_uppercase:
        upper=True
    elif char in string.ascii_lowercase:
        lower=True
    elif char in string.digits:
        digit=True
    elif char in string.punctuation:
        special=True

if length and upper and lower and digit and special:
    print("Strong Password")
else:
    print("Weak Password")
    if not length:
        print("Password should be atleast 5 characters long")
    if not upper:
        print("Password should contain atleast one uppercase letter")
    if not lower:
        print("Password should contain atleast one lowercase letter")
    if not digit:
        print("Password should contain atleast one digit")
    if not special:
        print("Password should contain atleast one special character")