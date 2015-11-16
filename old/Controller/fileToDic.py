"""this file is for reading in a file and sorting each new line into a dictionary"""

def fileToDic(str_fileName):
	dictionary = {}     #creates and empty dictionary
	index = 0
	with open(str_fileName) as file:        #opens the file and stores the file object with the name file
	    for line in file:
	        dictionary[index] = line.rstrip('\n')       #This adds each line into the dictionary and takes the newline off
	        index = index+1
        return dictionary       
