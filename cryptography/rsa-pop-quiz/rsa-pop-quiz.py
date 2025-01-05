from pwn import *
import gmpy2

host = "jupiter.challenges.picoctf.org"
port = 58617

r = remote(host, port)

# q1
output = r.recvuntil(b"IS THIS POSSIBLE and FEASIBLE? (Y/N):")
q = int([l for l in str(output).split('\\n') if 'q :' in l][0].split(':')[1].strip(), 10)
p = int([l for l in str(output).split('\\n') if 'p :' in l][0].split(':')[1].strip(), 10)
n = p * q

r.send(b"Y\n")
print("Sending Y and answer for n: {}".format(n))
r.send("{}\n".format(n))

# q2
output = r.recvuntil(b"IS THIS POSSIBLE and FEASIBLE? (Y/N):")

p = int([l for l in str(output).split('\\n') if 'p :' in l][0].split(':')[1].strip(), 10)
n = int([l for l in str(output).split('\\n') if 'n :' in l][0].split(':')[1].strip(), 10)

q = n // p
print("Sending Y and answer for q: {}".format(q))
r.send(b"Y\n")
r.send("{}\n".format(q))

# q3
output = r.recvuntil(b"IS THIS POSSIBLE and FEASIBLE? (Y/N):")
print("Sending N")
r.send(b"N\n")

# q4
output = r.recvuntil(b"IS THIS POSSIBLE and FEASIBLE? (Y/N):")
q = int([l for l in str(output).split('\\n') if 'q :' in l][0].split(':')[1].strip(), 10)
p = int([l for l in str(output).split('\\n') if 'p :' in l][0].split(':')[1].strip(), 10)

t_n = (p-1)*(q-1)

print("Sending Y and answer for t_n: {}".format(t_n))
r.send(b"Y\n")
r.send("{}\n".format(t_n))

# q5
output = r.recvuntil(b"IS THIS POSSIBLE and FEASIBLE? (Y/N):")
plaintext = int([l for l in str(output).split('\\n') if 'plaintext :' in l][0].split(':')[1].strip(), 10)
n = int([l for l in str(output).split('\\n') if 'n :' in l][0].split(':')[1].strip(), 10)
e = int([l for l in str(output).split('\\n') if 'e :' in l][0].split(':')[1].strip(), 10)
ciphertext = pow(plaintext, e, n)

print("Sending Y and answer for ciphertext: {}".format(ciphertext))
r.send(b"Y\n")
r.send("{}\n".format(ciphertext))

# q6
output = r.recvuntil(b"IS THIS POSSIBLE and FEASIBLE? (Y/N):")
print("Sending N")
r.send(b"N\n")

# q7
output = r.recvuntil(b"IS THIS POSSIBLE and FEASIBLE? (Y/N):")
q = int([l for l in str(output).split('\\n') if 'q :' in l][0].split(':')[1].strip(), 10)
p = int([l for l in str(output).split('\\n') if 'p :' in l][0].split(':')[1].strip(), 10)
e = int([l for l in str(output).split('\\n') if 'e :' in l][0].split(':')[1].strip(), 10)

t_n = (p-1)*(q-1)
d = gmpy2.invert(e, t_n)
print("Sending Y and answer for d: {}".format(d))
r.send(b"Y\n")
r.send("{}\n".format(d))

# q8
output = r.recvuntil(b"IS THIS POSSIBLE and FEASIBLE? (Y/N):")
p = int([l for l in str(output).split('\\n') if 'p :' in l][0].split(':')[1].strip(), 10)
ciphertext = int([l for l in str(output).split('\\n') if 'ciphertext :' in l][0].split(':')[1].strip(), 10)
e = int([l for l in str(output).split('\\n') if 'e :' in l][0].split(':')[1].strip(), 10)
n = int([l for l in str(output).split('\\n') if 'n :' in l][0].split(':')[1].strip(), 10)
q = n // p
t_n = (p-1)*(q-1)
d = gmpy2.invert(e, t_n)
plaintext = pow(ciphertext, d, n)
print("Sending Y and answer for plaintext: {}".format(plaintext))
r.send(b"Y\n")
r.send("{}\n".format(plaintext))

# q9
output = r.recvall()
print(output)

# answer
print(unhex(format(plaintext, 'x')))