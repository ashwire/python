# Datatype

number = 60  # int
num = 34.78  # float
greeting = "Hello there"  # str
isPythonInteresting = True  # bool


# A Variable with multiple values
languages = ["Python", "php", "java", "kotlin"]  # list
fruits =("apple","banana","pineapple") # Tuple
countries = {"Kenya","Ghana","China"} # set
# Dictionary
details = {
    "firstname" : "Ashley",
    "course" : "MIT",
    "age" : 18,
    "nationality" : "USA"
}

print(number)
print(num)
print(greeting)
print(countries)
print(details)
print(details["firstname"])
print(details["nationality"])

# Determining the data type of variable
print(type(details))
print(type(countries))
print(type(greeting))

# Typecasting - converting one datatype to another
print(float(number))
print(int(num))