num = int(input("Enter a number: "))

sum = 0

temp = num
while temp > 0:
    digit = temp% 10
    sum += digit ** 3
    temp //=10


if num == sum:
    print("num, is an Armstrong number")
else:
    print("num, is nit an Armstrong number")


#Input the value of terms
n = int(input("Enter the value of terms: "))


sum = 0 #intitialise
i = 1
while i<=n: 
    sum = sum+i
    i = i+1


print("\nSum = ", sum)

