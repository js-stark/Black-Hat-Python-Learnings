import hashlib

hashvalue = input('"enter a word to hash')

## MD5 Hasher
hashobj1 = hashlib.md5()
hashobj1.update(hashvalue.encode())
print("MD5 hashed value: ",hashobj1.hexdigest())

## SHA1 Hasher
hashobj2 = hashlib.sha1()
hashobj2.update(hashvalue.encode())
print("SHA1 hashed value: ",hashobj2.hexdigest())

## SHA224 Hasher
hashobj3 = hashlib.sha224()
hashobj3.update(hashvalue.encode())
print("SHA224 hashed value: ",hashobj3.hexdigest())

## SHA256 Hasher
hashobj4 = hashlib.sha256()
hashobj4.update(hashvalue.encode())
print("SHA256 hashed value: ",hashobj4.hexdigest())

## SHA512 Hasher
hashobj5 = hashlib.sha512()
hashobj5.update(hashvalue.encode())
print("SHA512 hashed value: ",hashobj5.hexdigest())



