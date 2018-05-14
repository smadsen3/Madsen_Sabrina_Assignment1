# Question 1
#!/usr/bin/env python3
import fileinput
import string
import os
# os.getcwd()
# a) find and replace words in a file
f2 = open("text.txt","r")
mystring=f2.read()
print mystring
# b) create a new directory within the working directory
directory = os.getcwd()
os.mkdir('copy') #make a new directory called directory
os.chdir('copy') #change to the new directory

new = string.replace(mystring,"dog","cat")
newfile = open('text.txt',"w")
newfile.write(new)
newfile.close()

os.chdir('../') #go up to previous directory
# Madsen_Sabrina_Assignment1
