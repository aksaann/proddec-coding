''' Program to find the roots of a quadratic equation.'''
import math #importing math module
#accepting the coefficients from the user
a=int(input("Enter coefficient a: "))
b=int(input("Enter coefficient b: "))
c=int(input("Enter coefficient c: "))


d = b * b - 4 * a * c #calculating the discriminant    

sqrt_val = math.sqrt(abs(d)) 
if a == 0: 
        print("Invalid") #If a is 0, then equation is not quadratic, but linear 
      
elif d > 0: 
        print("Roots are real and different ") 
        print((-b + sqrt_val)/(2 * a)) 
        print((-b - sqrt_val)/(2 * a)) 
elif d == 0: 
        print("Roots are real and same") 
        print(-b / (2*a)) 
else: #d<0 
        print("Roots are complex") 
        print(- b / (2*a) , " + i", sqrt_val) 
        print(- b / (2*a) , " - i", sqrt_val) 