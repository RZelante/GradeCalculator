"""
grade calculator
"""
print("grade calculator")
print("")

# find the the full path name to the GradeCalculator.py script file
# this could be something like C:\COSC1315\CH4\GradeCalculator.py
# the Python global variable __file__ stores the full path name for the currently executing script file
scriptFilePath = __file__

# the input file grade_input.txt will be located in the same folder as the GradeCalculator.py script file
# calculate the full path name to the grade_input.txt input file
# this could be something like C:\COSC1315\CH4\grade_input.txt
# use the replace member function to calculate the full path to the input file
inputFilePath = scriptFilePath.replace( "GradeCalculator.py", "grade_input.txt" )

# the output file grade_output.txt will be created in the same folder as the GradeCalculator.py script file
# calculate the full path name to the grade_output.txt input file
# this could be something like C:\COSC1315\CH4\grade_output.txt
# use the replace member function to calculate the full path to the output file
outputFilePath = scriptFilePath.replace("GradeCalculator.py","grade_output.txt")

# display the full path names for all files
print("This script file path is ", scriptFilePath) # the fully qualified script file name
print("This input file path is  ", inputFilePath)  # the fully qualified input file name
print("This output file path is ", outputFilePath) # the fully qualified output file name
 
# open grade_input.txt for input
fin  = open(inputFilePath,  "r")

# open grade_output.txt for output
fout  = open(outputFilePath, "w") 

# initialize variable for counting student file records
studentCount = 0

# initialize variable for computing average grade
totalGrade = 0

# process all file lines in a while loop
line = fin.readline() # read the first file line
while line != "":

    # split the line into its individual fields
    wordlist = line.split()

    # store the individual fields into variables
    # the first and last names are character data
    # the grade is an integer
    firstName = wordlist [0]
    lastName  = wordlist [1]
    grade     = int(wordlist [2])

    # calculate the letter grade
    if grade >= 90:
        letterGrade = "A"
    elif grade >= 80:
        letterGrade = "B"
    elif grade >= 70:
        letterGrade = "C"
    elif grade >= 60:
        lettergrade = "D"
    else:
        letterGrade = "F"

    # write data to the output file
    # put a space between each field
    # convert the grade to a string before writing it
    # put a new line character at the end of the line
    fout.write (firstName + " " + lastName + " " + str(grade) + " " + letterGrade + "\n")

    # update totals
    studentCount += 1
    totalGrade   += grade

    # read the next line
    line = fin.readline()

# close the input file
fin.close()

# close the output file
fout.close()

# output results
print("")
if studentCount == 0:
    print("no records in input file")
else:
    # calculate the average grade
    averageGrade = totalGrade / studentCount

    # output the record count
    print(studentCount, "records in the input file")

    # output the average grade with 1 fractional digit
    print("average class grade %.1f" % averageGrade)
    
    # list the contents of the grade_output.txt file
    print("")
    print("grade file contents:")
    
    # open the file for input
    fin = open(outputFilePath, "r")
    
    # read the contents of the file into a string
    text = fin.read()
    
    # output the string containing the file contents
    print (text) 
    
    # close the file
    fin.close()

# hold window open to allow user to view output
print("")
input("Press ENTER to continue ")
