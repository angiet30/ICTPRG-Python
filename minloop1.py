#a = [2.3, 7.9, -3.4, 4.2]
#print ("a: ", a)
##Initalise the counter variable
#i =0 #counter
##current minimum
#minval = a[0]
#while i<len(a):
#    print("minval:" , minval)
#    if a[i] < minval:
#        minval = a[i]
#    #print(a[i])
#    i = i+1
#print("final min val: ", minval)
#lst = []
#item = 0
#while item != "x":
#    item = input("Shopping list item: ")
#    if item == "x":
#        break
#    else:
#        lst.append(item)
#print(lst)
#
#search example
#Program to find an item in a string search
arr = ["hat", "watch", "baseball", "car", "pen"]
#Target
#targ = "Watch"
targ = ""
#for targ in arr:
#    if targ.lower() == "watch":
 #       print (targ)
#for k in range(len(arr)):
#    print(arr[k])
##### Ask user for a search input search for a string
### Put this into a while loop with "x" to end the search
while (True):
    targ = input ("Enter search word or press 'x' to exit: ")
    if targ == "x":
        break
    found =False
    i = 0 
    while (i<len(arr)):
        if targ.lower() == arr[i]:
            found = True
            print ("FOUND " + arr[i])
        i = i+1
    if found == False:
        print ("NOT FOUND, try again")


