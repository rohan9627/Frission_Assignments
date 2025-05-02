# Question 1
# Declare two variables, x and y, and assign them integer values. Swap the values of these variables without using any temporary variable.

a = 1
b=2 
print(f"value of a and b before swapping are a={a},b={b} ")

b = a+b
a = b-a
b = b-a

print(f"value of a and b after swapping are a={a},b={b} ")
############################################################################


# Question 2
# Create a program that calculates the area of a rectangle. Take the length and width as inputs from the user and store them in variables. Calculate and display the area.

l = int(input("enter the length of ractangle: "))
w = int(input("enter the width of ractangle: "))

area = l*w 
print(f"area of ractangle : {area}")

############################################################################


# Question 3
# Write a Python program that converts temperatures from Celsius to Fahrenheit. Take the temperature in Celsius as input, store it in a variable, convert it to Fahrenheit

c = float(input("enter the temp in celsius: "))

f= (c* 9/5)+32

print(f"temperature in fahrenheit is: {f}")
############################################################################


# Question 4
# Making function for split,upper,lower,strip,replace

def split(string,limiter=" "):
    a=[]
    temp=""
    for i in string:
        if i != limiter:
            temp+= i
        else:
            a.append(temp)
            temp=""
    a.append(temp)
    return a

x= split("rohan is, a boy"," ")
print(x)


######################################################
def replace(sentence,char,rchar):
    new=""
    for i in sentence:
        if i == char:
            new+=rchar
        else:
            new+=i
    return new

######################################################
def upper(s):
    result = ""
    for i in s:
        if 'a' <= i <= 'z':
            result += chr(ord(i) - 32)
        else:
            result += i
    return result
######################################################
def lower(s):
    result = ""
    for i in s:
        if 'A' <=i <='Z':
            result += chr(ord(i)+32)
        else:
            result+=i
    return
######################################################

def stripp(s):
    begin = 0
    end =len(s)-1
    while s[begin]==" " :
            begin+=1
    while s[end]==" ":
            end -=1
    return s[begin:end+1]

st = stripp(" rohan the cool doodh   ")
print(st)