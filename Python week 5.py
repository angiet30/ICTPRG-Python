#x7 = ["hat", 78, 2.3]
#for k in x7:
#    print() #new line
#    print( x7[0])
#    print( x7[1])
#    print( x7[2])
#x8 = [1,2,3] + [ 7,8,9]
#print (x8)
#msg = ["hello"] + ["world"]
#print (msg)
#x9 = x7 + [7,8,9]
#print(x9)
#num4 = [10] * 5
#print (num4)
#print()
#print ("range (start, sentinel, step)")
#num5 = list(range(1,20,3))
#for k in num5:
#    print(k)
#print ("num5:",num5)
#msg2 = "a qucik brown fox jumped over the lazy dog."
#l2 = msg2.split()
#print(l2)
#integers in string form
#num6 = "2 5 3"
#arr2 = num6.split()
#print(arr2)
#val = int(arr2[0]) #0 is the first element is 2
#print(val +3) #expecting 5
#### split command
ans5 = "Fred 20"
print(ans5)
ans6 = ans5.split()
print(ans6)
age = int(ans6[1])
print(age)
nm = ans6[0]
print("name: ", age)
#Extracting the age and converting it to an int
age = int(ans6[1])
print("age: ",age)
x = ["a","b","c"]
print(x)
print(x[0])
print(x[1])
print(x[2])
print()
print(x[-1])
print(x[-2])
print(x[-3])
num1 = [1,2,3]
num2 = [100,200,300]
print("num2", num2)
# a +=b is the same as a = a+b
num2 += num1
print ("num2: ",num2)
print()
##Appending to the end of the list
x = ['a']
print(x)
x += ['b']
print(x)
x += ['c']
print(x)
x.append('d')
print(x)
x.insert(1, 'ab')
print(x)
print()
# -4 -3 -2 -1
#  0  1  2  3
x2 = ['a','b','c','d']
print(x2)
x2.insert(-3,'v')
print(x2)
# .pop(k) deletes the kth element
x2.pop(0)
print(x2)
# delet the last element
x2.pop(-1)
print(x2)