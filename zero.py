n = int(input("Enter a number : "))
zeros = 0 #numbers of zeros in the product of the first n natural numbers
m=n
while n :
    zeros += n//5
    n//=5

print(f"The number of zeros in the product of the first {m} natural numbers is equal to { zeros }")
