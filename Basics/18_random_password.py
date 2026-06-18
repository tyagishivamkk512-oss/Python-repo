import random
import string

characters = string.ascii_letters + string.digits

password = ''.join(random.choices(characters, k=8))
#now it will take some random characters and will make 8 place password

print(password)