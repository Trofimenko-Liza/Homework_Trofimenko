
# task 1
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
e = float(input("Enter e: "))

if  ((a*a) + (b*b)) == ((c*c) + (e*e)):
    rectange_sqrt = a*b
    print("Rectange square is :", +rectange_sqrt)

elif a == b and b == c  and c == e and a ==c and a == e and b == e:
    print("It is square")

else:
    print("Incorrect value. It is not Rectange and not Square")

#square = lambda a = input("Enter a: "), b = input("Enter b: "),c = input("Enter c: "), e = input("Enter e: "): True  if a == b == c == e  (a**2)  else False
#print(square())