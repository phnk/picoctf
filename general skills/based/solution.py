from pwn import *
import gmpy2

def octal_to_str(octal_str):
    '''
    It takes an octal string and return a string
        :octal_str: octal str like "110 145 154"
    '''
    str_converted = ""
    for octal_char in octal_str:
        str_converted += chr(int(str(octal_char), 8))
    return str_converted


host = "jupiter.challenges.picoctf.org"
port = 29221

r = remote(host, port)

# q1 in the answer
output = r.recvuntil(b"Input:")
o = str(output).split("\\n")[1]
r.send("{}\n".format(o))

# q2 octa -> str
output = r.recvuntil(b"Input:")
o = octal_to_str([int(s) for s in str(output).split("\\n")[1].split(" ") if s.isdigit()])
r.send("{}\n".format(o))

# q3 hex to str
output = r.recvuntil(b"Input:")
o = bytearray.fromhex(str(output).split("\\n")[1].split(" ")[4:-3][0]).decode()
r.send("{}\n".format(o))

# q4 flag output
output = r.recvuntil(b"}\n")
print(output)