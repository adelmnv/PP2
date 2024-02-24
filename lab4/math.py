import math

#1
degree = float(input("Input degree: "))
radian = round(math.radians(degree),6)
print(f"Output radian: {radian}")

#2
def trapezoid_area(h,v1,v2):
    return (v1+v2)*h/2

h = float(input("Height: "))
first_v = float(input("Base, first value: "))
second_v = float(input("Base, second value: "))
area = trapezoid_area(h,first_v,second_v)
print(f"Expected Output: {area}")

#3
def polygon_area(n,l):
    area = round((n*l**2)/(4*math.tan(math.pi/n)),6)
    return area

n = int(input("Input number of sides: "))
l = float(input("Input the length of a side: "))
area = polygon_area(n,l)
print(f"The area of the polygon is:{area}")

#4
def parallelogram_area(l,h):
    area = l*h
    return area

l = float(input("Length of base: "))
h = float(input("Height of parallelogram: : "))
area = parallelogram_area(l,h)
print(f"Expected Output: {area}")

