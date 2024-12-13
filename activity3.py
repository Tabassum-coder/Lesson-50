#Write a Python program to remove lines of a file starting with prefix - Coding 
# and store the contents in a new file.

file1=open('Codingal.txt','r')
file2=open('UpdatedCodingl.txt','w')

for line in file1:
    if not(line.startswith('Coding')):
        file2.write(line)
file1.close()
file2.close()