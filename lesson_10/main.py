#input an integer value
n = int(input("Enter the number whose sum you want :"))
sum=0



#Iterates for n+1 times: i=1 to n+1
for i in range(1, n+1):
    sum = sum+i
    print("\nSum =", sum)
    
    
#Input a word or sentence
string = input("Pelease enter your own string")


string2 = ('')
#loop for printing in reverse
for i in string:
    string = i + string2
    

print("\nThe Original String =", string)
print("The Reveresed String = ", string2)