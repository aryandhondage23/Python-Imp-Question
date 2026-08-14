# 39)File handling with "With" function
#read the file using "with" function
with open('file.txt','r') as f:
    data=f.read()
    print(data)

# write the file using "with" function
with open('file.txt','w') as f:
    f.write("This is a sample text written to the file using 'with' function.")



# 40)what if try to read & unexisting file and what if in write mode

# 1. Read Mode ("r")
# If the file does not exist and you try to open it in read mode, Python raises a FileNotFoundError.
f = open("abc.txt", "r")


# 2. Write Mode ("w")
# If the file does not exist, Python creates a new file automatically.
f=open("abc.txt", "w")
f.write("hello")
f.close()




# 41)create one file with poem and read line by line
with open("poem.txt",'w') as f:
    f.write("Twinkle, twinkle, little star,\n")
    f.write("How I wonder what you are!\n")
    f.write("Up above the world so high,\n")
    f.write("Like a diamond in the sky.\n")

with open("poem.txt","r") as f:
    for line in f:
        print(line,end="")  # end="" is used to avoid adding extra newlines since lines already contain newline characters
# output:
# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.




# 42)In file there is one string give count of it
count=0
with open("poem.txt","r") as f:
    content=f.read()
    words=content.split()
    print("Total number of words in the file:", len(words))  # Output: Total number of words in the file: 20




# 43)How to delete file
import os
os.remove("poem.txt")  # This will delete the file named "poem.txt" from the current directory
print("File 'poem.txt' has been deleted.")