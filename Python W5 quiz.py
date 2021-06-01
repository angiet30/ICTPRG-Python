#values = [66,43,1,6,2,99,4]
#for k in values:
#    if k < 10:
#        print(k)

#DOB = input ("Date of Birth dd/mm/yyyy:  ")
#first_split, last_split = DOB.find("/"), DOB.rfind("/")
#day = DOB[:first_split]
#month = DOB[first_split+1:last_split]
#year = DOB[last_split+1:]
#print("Day: ",day)
#print("Month: ",month)
#print("Year: ", year)

#values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45, 78]
#Sum = sum(values)
#total = 0
#i = 0
#while i < len(values):
#    total += values[i]
#    i += 1
#Avg = total / len(values)
#Max = max(values)
#print("Sum is: ", Sum)
#print("Average is: ", Avg)
#print("Max is: ", Max)

#FullName = input("Please enter your fullname: ")
#name=FullName.split()
#initial= [letter [0].upper() for letter in name]
#print(''.join(initial)) 

#lst = [ ]
#number = 0
#while number != 'x':
#    number = input("Enter some number: ")
#    if number == 'x':
#        break
#    else:
#        lst.append(int(number))
#print (lst)

#number = input ("Enter a large number:  ")
#n = [int(i) for i in str(number)]
#Sum = sum(n)
#print(Sum)
lst = [ ]
newlst = [ ]
number = 0
while number != 'x':
    number = input("Enter a number:")
    if number == 'x':
        break
    else:
        lst.append(int(number))
def Repeat(x):
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[i] == x[j] and x[i] not in newlst:
                newlst.append(x[i])
    return newlst
print("Repeating Numbers: ", Repeat(lst))