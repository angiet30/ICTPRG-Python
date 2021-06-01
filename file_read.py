# Read a text file and print it
#file1=open("days02.txt")
#lines = file1.readlines()
#for line in lines:
#    print(line)
#    file1.close
infile=open('numbers.txt','r')
num1=int(infile.readline())
num2=int(infile.readline())
num3=int(infile.readline())
infile.close()
total=num1+num2+num3
print ('the numbers are ', num1, num2, num3)
print ('the total is ', total)