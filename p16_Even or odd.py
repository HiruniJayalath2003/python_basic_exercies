# Problem 16_Even or odd
num=int(input("Enter a number :"))
#calculation
remainder =num%2

if( remainder==0):
    print(f"{num} is Even number")
else:
    print(f"{num} is Odd number.")