inp = "jU5t_a_sna_3lpm18gb41_u_4_mfr340"
arr = [None] * 32

for i in range(31, 16, -2):
	arr[i] = inp[i]

for i in range(16, 32, 2):
	arr[i] = inp[46-i]

for i in range(8, 16, 1):
	arr[i] = inp[23-i]

for i in range(0, 8, 1):
	arr[i] = inp[i]

print(arr)

output = ""

for i in range(0, len(arr)):
	output += arr[i]

print(output)