import hashlib
import sys

# Function to compute SHA-256 hash
def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest() 

# The first argument is the password_hash.txt file
with open(sys.argv[1], 'r') as password_file:
    password_hash = password_file.read().strip()
    print(f"Expected password hash: {password_hash}")

# The second argument is the rockyou_1.txt file
with open(sys.argv[2], 'r', encoding='utf-8', errors='ignore') as rockyou:
    for line_number, line in enumerate(rockyou, start=1):
        # Remove trailing newline and carriage return characters
        stripped_line = line.rstrip('\n').rstrip('\r')

        # Compute the SHA-256 hash of the stripped line
        hash_value = sha256_hash(stripped_line)

        # Check if the hash value matches the password hash
        if password_hash == hash_value:
            print(f"Password found: '{stripped_line}' (Line {line_number})")
            break
