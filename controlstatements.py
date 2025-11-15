num=int(input("Enter a number:"))

if num%2==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

#if elif else statement
marks=int(input("Enter your marks:"))
if marks  >=80 and marks <=100:
    print(f"{marks} is an A")
elif marks >=60 and marks <79:
    print (f"{marks} is a B")
elif marks  >=50 and marks <=69:
    print(f"{marks} is an C")
elif marks  >=40 and marks <=59:
    print(f"{marks} is an D")
elif marks  >=40 and marks <=49:
    print(f"{marks} is an D")
else:
    print(f"{marks} is a fail")