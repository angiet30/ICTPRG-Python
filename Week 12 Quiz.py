
#### Question 1####
## Write the function between the START and END tags
## START
#def AddTwoNumbers(num1,num2):
#    return num1+num2
## END
## -------------------------------------
## DO NOT TOUCH ANY CODE BELOW THIS LINE
#print("Test 1 Passed: " + str(AddTwoNumbers(1, 2) == 3))
#print("Test 2 Passed: " + str(AddTwoNumbers(5, 6) == 11))
#print("Test 3 Passed: " + str(AddTwoNumbers(9, 0) != 10))

#### Question 2 ####
# Write the function between the START and END tags
# START
#def AddInString(x,y,z):
#    return (x+y+z)

# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
#print("Test 1 Passed: " + str(AddInString("Hello, ", "bob", ". How are you today?") == "Hello, bob. How are you today?"))
#print("Test 2 Passed: " + str(AddInString("Woah there ", "frank", ", watch your step!") == "Woah there frank, watch your step!"))
#print("Test 3 Passed: " + str(AddInString("Whats the , ", "meaning", " of all of this?") != "What is the meaning of all of this"))
#print("Test 4 Passed: " + str(AddInString("Happy ", "Lappy", " Tappy") == "Happy Lappy Tappy"))

####### Question 3 #######
# Write the function between the START and END tags
# START

#def FibonacciAdder(n):
#  sum = 0
#  fib1 = 0
#  fib2 = 1
#  fib3 = 0
#  for i in range (1,n):
#      fib3 = fib1 + fib2
#      fib1 = fib2
#      fib2 = fib3
#      sum += fib1
#  return sum

# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
#print("Test 1 Passed: " + str(FibonacciAdder(2) == 1))
#print("Test 2 Passed: " + str(FibonacciAdder(5) == 7))
#print("Test 3 Passed: " + str(FibonacciAdder(10) == 88))

####### Question 4#######
# Write the function between the START and END tags
# START
#def MultiplyElementsInlist(list):
#    answer = 1
#    for x in list:
#        answer *= x
#    return answer
# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
#print("Test 1 Passed: " + str(MultiplyElementsInlist([1, 2, 3]) == 6))
#print("Test 2 Passed: " + str(MultiplyElementsInlist([0, 2, 3]) == 0))
#print("Test 3 Passed: " + str(MultiplyElementsInlist([2, 2, 2]) == 8))
#print("Test 4 Passed: " + str(MultiplyElementsInlist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 30414093201713378043612608166064768844377641568960512000000000000))


####### Question 5 #####
# Write the function between the START and END tags
# START
#def IsPalindrome(string):
#    string = string.lower()
#    string = string.replace(" ",'')
#    text = string [::-1]  #### create text in reverse start and then end, if +ve will start from left
#    return string == text
# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
#print("Test 1 Passed: " + str(IsPalindrome("GlenElg") == True))
#print("Test 2 Passed: " + str(IsPalindrome("Nurses Run") == True))
#print("Test 3 Passed: " + str(IsPalindrome("Nurses") == False))
#print("Test 4 Passed: " + str(IsPalindrome("frank") == False))

######## Question 6 ###########
# Write the function between the START and END tags
# START
#def SortWordsAlphabetically(word):
#    word = word.lower()
#    alpha = word.split('-')
#    alpha.sort()
#    return "-".join(alpha)
# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
#print("Test 1 Passed: " + str(SortWordsAlphabetically("Bob-does-not-like-frank") == 'bob-does-frank-like-not'))
#print("Test 2 Passed: " + str(SortWordsAlphabetically("why-am-i-doing-this-this-is-terrible") == "am-doing-i-is-terrible-this-this-why"))
#print("Test 3 Passed: " + str(SortWordsAlphabetically("frank-kill-zoe-did") == "did-frank-kill-zoe"))

###### Question 7######
def PrintBoxByWidth(width, height):
    for row in range (height):
        for col in range (width):
            if ((col == 0 or col == width -1) or (row == 0 or row == height -1)):
                print ("x", end="")   #### print the height
            elif (row == height-1)/2 or ((height % 2 == 0) and row == (height/2) or row == (height/2 -1)):
                print ("o", end= '') ### print a space for the widtch
            else: 
                print (" ", end='')
        print ("")  # print new line
PrintBoxByWidth(60, 5)
