### y = x * x mathematical function
def square (x):
    return x*x

print ( square(2))
print ( square(4))

def dist(x,y):
    return x*x + y*y
print()
print( "(1,1): ", dist(1,1) )
print( "(2,4): ",dist(2,4))

def dist2(x,y):
    return square(x) + square(y)
print (dist2(2,4))

#### 2021-05-28
#####  formatdate (2021,5,28)
#year = input("Enter year: ")
#month = input("Enter month: ")
#date = input("Enter day: ")
def formatDate(year,month,day):
    s1 = str(year) + "-"
#    print(s1)
    if 0 <= month < 10:
        s1 += "0"
    s1 += str(month)
    s1 += "-"
#    print(s1)
    if 0 <= day < 10:
        s1 += "0"
    s1 += str(day)
    print (s1)
formatDate (2021,5,28)

#### Define main function
def main():
    #get_name()
        print ("Hello", get_name())

###Definition of the get_mame function
def get_name():
    name = input ("Enter your name: ")
    return name
        
### Call the main function
main()




