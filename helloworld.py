print("Hello World")

# Variables
Name = "John"
Age = 20
Status = "New"

print(Name, Age, Status)

#input
name = input("What is your name?   ")
print ('Hi' , name)
print ("hi  " + name)

name = input("Hi welcome, what is your name?  ")
colour = input ("what is your favourite colour?  ")
print (name + '  likes  ' + colour)

birth_yr = input("Whats your birth year?  ")
age = 2025 - int(birth_yr)
print("Your age is " , age)

weight = input('What is your weight in pounds?  ')
weight_kg = int(weight) * 0.45
print("Your weight is " , weight_kg, 'kg')


course = '''Python's course for begginers 
Learn everyday
Practice evryday'''
print(course)
print(course[0:])
print(course[:])
print(course[1:])
print(course[1:3])
print(course[-1])
print(course[-2])
print(course[1:-1])






