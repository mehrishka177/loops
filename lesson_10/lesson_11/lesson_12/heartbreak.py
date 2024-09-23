num = int(input("Enter the number :"))
t = num
numLen = 0 
while t>0:
    numLen = numLen+1
    t = int(t/10)
    
    
    if numLen>=4:
        num = int(numLen/2)
        chk = 0
        while num>0:
            rem = num%10
            if chk==numLen:
                midOne = rem             
            elif chk==(numLen-1):                
                midTwo = rem                
            num = int(num/10)            
            chk = chk+1            
        prod = midOne*midTwo       
        print("\nProductof Mid digits(" +str(midOne)+ "*" +str(midTwo)+")=", prod)
              
    else:
                  print("\nIt's not a 4 more than 4-digit number!!")
            