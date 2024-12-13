#read its contents
file=open('Codingal.txt','r')
print(file.read())
file.close()

#read only the first 8 characters
file=open('Codingal.txt','r')
print(file.read(8))
file.close()

#append name to the file
file=open('Codingal.txt','a')
file.write('\nTabassum')
file.close()

file=open('Codingal.txt','r')
print(file.read())
file.close()