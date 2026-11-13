i = 2 
n = int(input("Enter a number : "))
div_sum = 1

while i*i<=n : 
    if n%i==0:
        div_sum+=i
        if i*i!=n:
            div_sum+=(n//i)
    i+=1

if n==1:
    print("1 is NOT a perfect number")
elif div_sum==n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is NOT a perfect number")