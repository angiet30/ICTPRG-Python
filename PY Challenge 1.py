import datetime
today = datetime.datetime.now()
firstname = ''
while True:
    firstname=input("Enter your FirstName: ")
    if not firstname:
        break
    else:    
        lastname=input("Enter your LastName: ")
        Age = int(input("Enter your Age:  "))
        username = firstname[0].lower()+lastname.lower()
        pwinitial= firstname.lower()+lastname[0].upper()
        yob = today.year - Age  #no offset as 3rd last digit of my studend id is a 0
    print(username+"@Huawow.io"+"|"+pwinitial+"_"+str(yob))