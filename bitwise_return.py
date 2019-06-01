"""Given three 32-bit integers x, y, and b, return x if b is 1 and
 y if b is 0, using only mathematical or bit operations.
  You can assume b can only be 1 or 0."""

def return_bit(x, y, b):
    if b & 1:
        return x
    else:
        return y


x = input("Enter x: ")
y = input("Enter y: ")
b = int(input("Enter 0 or 1: "))
print(return_bit(x, y, b))
