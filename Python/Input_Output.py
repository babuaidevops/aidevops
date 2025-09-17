print("hello Dasta")

###########
'''
name = input("Enter your name: ")
print("Hello,", name ,"! welcome")
print(f"Hello,", name ,"! welcome")

############

s = "Dastagiri"
print(f"Your string is : {s}")

############

a = 10
b="Giri"
c=20.5

print(f"Value of a,b & c are {a}, {b}, {c}")

#### Multiple Inputs ######

x, y = input("Enter two values: ").split()
print(f"Value of x is {x}")
print(f"Value of y is {y}")

########Print Numbers######

n = int(input("Enter any number"))
print(n) #ValueError: invalid literal for int() with base 10 : 'giri' if we pass string

price = float(input("Enter float value : "))
print(price)

a = "Hello Dasta"
b = 10
c = 11.22
d = ("Hi", "Dasta", "Welcome")
e = ["Hi", "Dasta", "Welcome"]
f = {"Hi": 1, "for":2, "Welcome":3}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

p=q=r=100
print(p,q,r)

x,y,z=10,20.5,"Dasta"
print(x,y,z)


# Casting variables
s = "10"  # Initially a string
n = int(s)  # Cast string to integer

print(n)

cnt = 5
f = float(cnt)  # Cast integer to float
print(f)

age = 25
s2 = str(age)  # Cast integer to string
print(s2)

n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
bool = True

# Get and print the type of each variable
print(type(n))   
print(type(f)) 
print(type(s))   
print(type(li))     
print(type(d))     
print(type(bool))

x = 5
print(x) 

del x # Delete a Variable Using del Keyword

print(x) # NameError: name 'x' is not defined

'''
#Swapping Two Variables

a, b = 5, 10
a, b = b, a

print(a,b)

#Counting Characters in a String
word = "Hello Dastagiri"
leng = len(word)

print("Length of the word:" leng)
print(f"Length of the word:", {leng})







