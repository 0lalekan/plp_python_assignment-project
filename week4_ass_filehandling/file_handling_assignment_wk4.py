# program that reads a file and writes a modified version to a new file.
file1 = open("myfile.pdf", "r")   #reading the file
content = file1.readlines()

file2 = open("copy.txt", "w")      #writing to a new file
for line in content:
    file2.write(line.upper())     #modifying the content to uppercase

file1.close()
file2.close()

# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
fileName = input("Enter the file name: ")   #requesting user input
try:
    with open(fileName, "r") as file:      #using 'with' to handle file     
        content = file.readlines()
        print(content)

except FileNotFoundError:                                 #handling file not found error
    print("File not found. Please check the file name.")  