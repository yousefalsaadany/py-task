import math 

print("-------------task1-------------")
# task 1(Calculate the simple interest using the formula I = P * r * t)
p=float(input("plz enter the principal amount: "))
r=float(input("plz rnter the  rate of interest: "))
t=float(input("plz enter the time in years: "))
l=p*r*t
print("the simple interest=",l)
#------------------------------------------------------------------------
print("-------------task2-------------")
# task 2(Using the Pythagorean theorem, find the length of the hypotenuse)
a=float(input("plz enter the hight : "))
b=float(input("plz enter the Base length : "))
c=math.sqrt((math.pow(a,2)+math.pow(b,2)))
print("the length of the hypotenuse= ",c)
#------------------------------------------------------------------------
print("-------------task3-------------")
#task 3(Print a String 5 Times, each in a separate line)
text=input("plz enter string: ")
print((text+"\n")*5)
