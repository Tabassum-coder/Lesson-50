#read first line of the file

file=open('Codingal.txt','r')
print(file.readline())
file.close()

#read first 3 lines
file=open('Codingal.txt','r')
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file=open('Codingal.txt','r')
for line in file:
    print(line)

file.close()