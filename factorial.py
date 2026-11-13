n = int(input("Enter a number : "))
a = 1

for i in range(2 , n+1):
    a*=i

print(f"the product of the first {n} numbers is equal to {a}")