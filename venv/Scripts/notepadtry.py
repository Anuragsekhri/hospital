import os

file = open("D:/patientsdata/1.txt","wt")
file.write("hey Anurag Sekhri")
file.close()
#the above code creates a text file n yea that ol the lines u need to write data
#writing the stuff i need in enterpatientfile

#i need to read the file in predict.py

file = open("D:/patientsdata/1.txt", "r")
for each in file:
        print(each) #this thing is printing on cmd i want the file to be opened

os.system("D:/patientsdata/1.txt") #this line did it.....
