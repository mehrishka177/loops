def factorial(x):


   if x==0 or x==1:
       return 1
   else:
       return x*factorial(x-1)
   
print("the factorial of 0:", factorial(0))
print("the factorial of 1:", factorial(1))
print("the factorial of 2:", factorial(4))
print("the factorial of 5:", factorial(5))
print("the factorial of 10:", factorial(10))