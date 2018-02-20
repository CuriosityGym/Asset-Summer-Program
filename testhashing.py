import hashlib
h = hashlib.md5()
h.update("fgA43!OO2".encode())
h.hexdigest()
print(h.hexdigest())
