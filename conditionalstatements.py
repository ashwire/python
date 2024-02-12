temperature = 32

if temperature> 37:
    print("it is hot")
else:
    print("it is cold")

# A program that prints the largest number among three numbers
num1 = 45
num2 = 89
num3 = 32
if num1> num2 and num1> num3:
    print(num1,"is the largest number")
elif num2 > num1 and num2 > num3:
     print(num2,"is the largest number")
else:
    print(num3,"is the largest number")

# A program that checks whether a number is even or odd
number = 56
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

#(assign)a program that checks whether a number is prime or not
x = 23
y = 30

if x/2 and 3 and 6 and 7== 1:
    print("false")
else:
    print("prime")
if y/2 or 5 == 15 or 6:
    print("false")
else:
    print("prime")


num= int(input("Enter a number"))
if num > 1:
    for i in range (2, num):
        if num % i == 0 :
            print("not a prime number")
            break
    else : print("is a prime number")
else : print("not a prime number ")