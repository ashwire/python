# Inbuilt functions
y = max(67,56,34,25,78)
print(y)

x = min( 12,45,90,5)
print(x)

z = pow(2, 3)
print(z)

# user defined functions
def details():
    print("Ashley")
details()# Calling a function

# Parameters and argument
def students(name,course,age):
    print(name,course,age)

students("Ashley", "MIT", 17)
students("Goretty", "Cybersecurity", 18)


def Employees(fullname,IDno,salary,position,age):
    print(fullname,IDno,salary,position,age)

Employees("Rose", 123456, 120000, "Marketing manager", 34)
Employees("Kinyua", 123456, 342000, "CEO", 55)
Employees("Mbappe", 123456, 112000, "Secretary", 28)
Employees("Wafula", 123456, 123000, "Accountant", 36)
Employees("Nyanchoka", 123456, 165000, "HR manager", 45)