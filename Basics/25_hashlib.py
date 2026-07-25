import hashlib

def make_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify(attempt,stored):
    if(make_password(attempt) == stored):
        return True
    else:
        return False


password = "shivam tyagi"
stored = make_password(password)

attempt = input("enter password: ")
if verify(attempt,stored):
    print("logged in successfully")
else:
    print("password incorrect")