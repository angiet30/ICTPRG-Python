#outfile=open('student.txt','w')
#outfile.write('Philip Locke\n')
#outfile.write('David Beckett\n')
#outfile.write('Edmun Burke\n')
#outfile.close()
#infile=open('student.txt','r')
#file_contents=infile.read()
#print(file_contents)
#infile.close()
###### Read line######
L = ['London\n', 'Canberra\n','Seoul\n']
file1=open('myfile.txt','w')
file1.writelines(L)
file1.close()
file1=open('myfile.txt','r')
Lines=file1.readlines()
print(Lines)

count = 0
##### Strip the newline character
for line in Lines:
    print(line.strip())
    count = count + 1
    print("Line {}: {}".format(count,line.strip()))


#L = ['One\n', 'Two\n', 'Three\n']
#with open('numbers.txt','w') as fp:
#    fp.writelines(L)
#count = 0
#print ("Using readlines() to read to file")

#with open("numbers.txt") as fp2:
#    lines = fp2.readlines()
#fp2.close()
#for line in lines:
#        count += 1
#        print("Line{}: {}".format(count, line.strip()))
####### Using readline()
#count = 0 
#print('nUsing readline()')

#with open('numbers.txt') as fp:
#    while True:
#        count += 1
#        line = fp.readline()

#        if not line:
#            break
#        print("Line{}: {}".format(count, line.strip()))

## Using for loop
#count = 0
#print ("\nUsing for loop to iterate")

#with open ("numbers.txt") as fp2:
#    for line in fp2:
#        count +=1
#        print("Line{}: {}".format(count, line.strip()))