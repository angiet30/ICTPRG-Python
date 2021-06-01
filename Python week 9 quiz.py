##### Q1####
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = int(num1) + int(num2)
outfile = open("maths.txt",'w')
outfile.write(str(sum))
outfile.close()

#### Q2#####
lst = []
name = ''
while True:
    name = input("Enter your name: ")
    if not name:
        break
    else: 
        lst.append(name)
print (lst)
with open ('people.txt', 'w') as fp:
    for line in lst:
        fp.write(f'{line}\n')

#######Q3#######
with open('name.txt','r') as infile:
    y = infile.read().lower()
    print(y)
with open('name.txt','r') as infile:
    y = infile.read().title()
with open('nameformatted.txt','a') as outfile:
    outfile.write(y) 
    print(y)

###### Q4######
count = 0
lst = []
import math
for i in range (1, 10):
    f = math.factorial(i)
    count +=1
    lst.append(count)
    print(i, "=",lst,"->", f)

####Q5#####
lst1=[]
lst2=[]
def auth():
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    lst1.append(username)
    lst2.append(password)
    with open('logins.txt','r') as f:
        for line in f:
            logininfo = line.strip().split(":")
            if username == logininfo[0] and password == logininfo [1]:
                return True
        return False
if auth():
    print("Access granted!, ", "username: ",lst1,"password:", lst2)
else:
        input("no Access")