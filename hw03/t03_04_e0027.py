n = int(input())

binary_str = bin(n)[2:]
max_m = 0

for i in range(len(binary_str)):
    shifted_str = binary_str[i:] + binary_str[:i]
    current_m = int(shifted_str, 2)
    if current_m > max_m:
        max_m = current_m

print(max_m)