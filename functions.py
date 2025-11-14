def myfunction():
    print("this is my first function")
myfunction()

# function with parameters
def students(name,age,gender):
    print(f"Student na is a {name} ")
    print(f"Student age is  {age}")
    print(f"student gender is {gender}")
students("callagan",43,"male")

def add_numbers(a,b):
    return a+b
result= add_numbers(3,5)
print(result)