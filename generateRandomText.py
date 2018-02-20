import random
import string

digits = "".join( [random.choice(string.digits+string.ascii_letters+string.ascii_uppercase) for i in range(2000)] )
print (digits)
