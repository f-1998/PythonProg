#faulty calculator

op = input("enter the operator")
x = int(input("enter the first no."))
y = int(input("enter the second no."))

if op == "*":
    if x == 3 and y == 4:
        print(77)
    else:
        print(x*y)
elif op == "+":
     if x == 5 and y == 7:
         print(56)
     else:
         print(x+y)
elif op == "-":
    if x == 8 and y == 9:
        print(4)
    else:
        print(x-y)

else:
    if x == 12 and y == 6:
        print(4)
    else:
        print(x/y)