#Take a number as input from the user.
#Calculate the sum of its digits.
#Print the result.
num=int(input("enter number "))
sum=0
while num > 0:
    sum+=num % 10
    num//=10
print("Sum of digits : ",sum)    
