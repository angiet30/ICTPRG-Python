###### Question 1  #########
#validInteger = False
#while not validInteger:
#    number = input ("Enter a number: ")
#    if number.isdigit():
#        validInteger = True
#    else:
#        print ("Must a valid number")
#print ("your number is s" + str(number))

####### Question 2 ######### 
#lst = []
#while True:
#    try:
#        word = input("Enter a word: ")
#        if len(word) > 2 and len(word) <6:
#            lst.append(word)
#        else:
#            print("Invalid word")
#            print (lst)
#            break
#    except:
#        continue

##### Question 3 #####
#import re
#regex = '^[A-Za-z0-9]+[\.]?[A-Za-z0-9]+[@]\w+[.]\w{2,32}$'
#def main():
#    email = input("Enter your email: ")
#    while True:
#        if(re.search(regex,email)):
#            print("Valid Email")
#        else:
#            print("Invalid Email")
#            break
#    email = input("Enter your email: ")
#if __name__ == '__main__':
#    main()


###### Question 4##### I
#import ipaddress
#def validate_ipaddress(ip):
#    try:
#        ipaddress.ip_address(ip)
#        return True
#    except ValueError as errorCode:
#        pass
#        return False
#def main():
#    ipaddr=input("Please enter an ip address: ")
#    while True:
#        if(validate_ipaddress(ipaddr)==False):
#            print("This is an invalid address.")
#        else:
#            print("IP address {} is valid".format(ipaddr))
#            break
#        ipaddr = input("Please enter an ip address: ")
#if __name__ == "__main__":
#    main()

#### Question 5####
import re
while True:
    p = input("Input your password:  ")
    is_valid = False
    if (len(p)< 7):
        print ("Not a Valid password")
        continue
    elif not re.search("[a-z]",p):
        print ("Not a Valid password")
        continue
    elif not re.search("[0-9]",p):
        print ("Not a Valid password")
        continue
    elif not re.search("[A-Z]",p):
        print ("Not a Valid password")
        continue
    elif not re.search("[$#@)*(!]",p):
        print ("Not a Valid password")
        continue
    elif p != "password":
        print ("Not a Valid password")
        continue
    else:
        is_valid = True
        break
if (is_valid):
    print("Password is valid")
        
        
