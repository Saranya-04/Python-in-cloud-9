import re
#Open file to read
f = open('preproinsulin-seq.txt','r')

#Open file to write
fc = open('preproinsulin-seq-clean.txt','w')

#To filter lower case letters
ma = re.findall(r"[a-z]+",f.read())
print(ma)

#To write to a file
for element in ma:
   fc.write(element)
fc.close()

#To couth the characters
clean_fc = open('preproinsulin-seq-clean.txt','r')
length = clean_fc.read()
if len(length)==110:
    print("The cleaned file has 110 character")
else:
    print("Sorry, the file doesn't have 110 characters")
    


