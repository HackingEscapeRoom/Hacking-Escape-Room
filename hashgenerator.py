import hashlib

# Passwort, das gehasht werden soll
password = "password"

# MD5-Hash
md5_hash = hashlib.md5(password.encode()).hexdigest()
print(f"MD5: {md5_hash}")

# SHA1-Hash
sha1_hash = hashlib.sha1(password.encode()).hexdigest()
print(f"SHA1: {sha1_hash}")

# SHA256-Hash
sha256_hash = hashlib.sha256(password.encode()).hexdigest()
print(f"SHA256: {sha256_hash}")
