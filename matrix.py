print("--- 2x2 Matrix Determinant Calculator ---")

a = int(input("enter 'a' (top left): "))
b = int(input("enter 'b' (top right): "))
c = int(input("enter 'c' (bottom left): "))
d = int(input("enter 'd' (bottom right): "))

determinant = (a * d) - (b * c)
print(f"The determinant is: {determinant}") 

