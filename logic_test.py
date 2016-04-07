import math
import random
import sys

#import module for system path
import sys

x = 1
y = 2
print( x is y)

w = input("enter of you choice 1")
q = input("enter a number of your choice 2")

print (w is q)

#print a square root of a number 4
x = 4
p = int( math.sqrt(x))
print(p)



def area_t(h,b,c):
    k = (0.5*h)*(b+c)
    return k
print (area_t(4,4,3))

def quadratic_e(q,p,r,d):
    z = ((q*pow(p,2))+(r*p)+d)
    return z
print(quadratic_e(2,2,2,2))

#function for swapping 2 numbers without creating a temporary a variable

def swap(var1,var2):
    print("Before swap")
    print("var1",var1)
    print("var2",var2)
    print("after swap is done")
    var1= var1+var2
    var2 =var1-var2
    var1= var1-var2
    print("var1",var1)
    print("var2",var2)
    return
swap(2,3)

# a function that prints a random module
def generate_r():
    y = random.randint(1,7)
    print( "random number is :",y)
    return
generate_r()

# a function for converting kilometers into miles
def convert_kilo_miles(kilo):
    miles = float(1000*kilo)
    print("converting kilometer into miles: ",miles,"miles")
    return
convert_kilo_miles(200)

def check_positive():
    numb = float(input("enter a number to be checked:"))
    if numb > 0:
        print(numb,"Is  a positive number")
    elif numb == 0:
        print ("Zero")
    else:
        print(numb,"number is negative ")
    return
check_positive()

vars = 5*4
varp = 5**4
print(varp,vars,pow(5,4))

#string concatenation

num = str(18)
num3 = 18
print("bucky is "+ num +`num3`)

#list and sequence

family =['mom','dad','bro','sis','dog']
print(family[3])
#silicing
example = [0,1,2,3,4,5,6,7,8,9]
print(example[4:8])
print(example[-4:-8])
print(example[-5:])
print(example[:])
print(example[1:9:2])
print(example[::-2])

#the build in  in-word function

name = 'solomon'
if 'z' in name:
    print("true")
else:
    print("try again")

print(name.count('o'),'solomon')

#checking for odd or even numbers

h = int(raw_input("Enter the any number:"))
if h%2 == 0:
    print h,"ia an even number"
else:
    print h,"is an odd number"

#program to find out the largest number among 3 numbers

x = int(raw_input("enter first number:"))
t = int(raw_input("enter second number:"))
k = int(raw_input("enter third number:"))
if (x > t) & (x >k):
    print x,"is greater than all the 2 numbers"
elif (t > x) & (t>k):
    print t,"is greater than all combined"
else:
    print k,"is greater than all them"


# simple multiplication table

num = int(raw_input("Enter number:"))

for i in range(1,11):
    print num ,"x", i,"=", num*i

#printing prime numbers between 1 and 10
lower = int(raw_input("lower range"))
upper = int(raw_input("upper range"))
for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
    else:
        print num



#print the directory for the system path depending the environment variable
print sys.path















