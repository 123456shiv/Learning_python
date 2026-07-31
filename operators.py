a = 10
b = 7


print(f"Bitwise AND (a & b): {a & b}")
print(f"Bitwise OR  (a | b): {a | b}")
print(f"Bitwise XOR (a ^ b): {a ^ b}")
print(f"Bitwise NOT (~a)   : {~a}")
print(f"Bitwise NOT (~b)   : {~b}")

temp = a
a = b
b = temp

print("\n--- After Swap ---")
print(f"Value of a: {a}")
print(f"Value of b: {b}")