#name = "bob"
#password = "password1234"
username = input("Enter Username: ")
username = username.upper()
userpassword = input("Enter Password: ")
userpassword = userpassword.lower()
if username ==  "BOB" and userpassword == "password1234":
    print ("Access Granted!")
elif username == "FRANK" and userpassword == "invalidpass":
    print ("Access Denied!")


  