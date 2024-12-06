def slope_cubic(a,b,c,d,x):
    slope = (3*a*x*x)+(2*b*x)+c
    return slope
a = float(input("Enter the coefficient of x^3 : "))
b = float(input("Enter the coefficient of x^2 : "))
c = float(input("Enter the coefficient of x : "))
d = float(input("Enter the value of constant term : "))
x = float(input("Enter the value of x at which slope is to be calculated : "))
s=slope_cubic(a,b,c,d,x)
print(s)