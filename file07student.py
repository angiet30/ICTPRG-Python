#outfile=open('student.txt','w')
#outfile.write('Philip Locke\n')
#outfile.write('David Beckett\n')
#outfile.write('Edmun Burke\n')
#outfile.close()
infile=open('student.txt','r')
file_contents=infile.read()
print(file_contents)
infile.close()