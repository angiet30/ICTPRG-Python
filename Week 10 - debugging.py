##### QUestion 1####
#greeting = input("hello possible pirate! What's the password?")
#if greeting in ['Arrr!']:
#    print('Go away, pirate. ')
#else:
#    print('Greetings, hater of pirates')

#### Question 2####
authors = (
    'Charles Dickens: 1870',
    'William Thackeray: 1863',
    'Anthony Trollop: 1882',
    'Gerard Manley Hopkis: 1889',
)
for comp in authors:
    new = comp.split(':')
    print (new[0],'die in',new[1])

###### Question 3  #####
#year = int(input("Greetings! What is your year of origin? '"))
#if year <= 1900:
#    print ("Woah, That's the past")
#elif year > 1900 & year < 2020:
#        print ("That's totally the present!")
#else:
#    print ("Far out, that's the future!!")

##### Question 4 ######
#exam_one = int(input("Input exam grade one: "))
#exam_two = int(input("Input exam grade two: "))
#exam_three = int(input("Input exam grade three: "))
#grades = [exam_one, exam_two, exam_three]
#sum = 0
#for grade in grades:
#  sum = sum + grade
#avg = sum / len(grades)
#if avg >= 90:
#    letter_grade = "A"
#elif avg >= 80 and avg <= 90:
#    letter_grade = "B"
#elif avg >= 70 and avg <= 79:
#    letter_grade = "C"
#elif avg <= 60 and avg <= 69:
#    letter_grade = "D"
#elif avg <= 0 and avg <=59:
#    letter_grade = "F"

#for grade in grades:
#    print("Exam: " + str(grade))
#    print("Average: " + str(avg))
#    print("Grade: " + letter_grade)

#if letter_grade == "F":
#    print ("Student is failing.")
#else:
#    print ("Student is passing.")

