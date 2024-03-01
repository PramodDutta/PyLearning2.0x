# File Handling
# How to Read a Text, and Write into it using python Code.


# Function -
# open("file_name","mode")

# Mode -
# 'r' for reading (default).
# 'w' for writing (creates a new file or truncates an existing one).
# 'a' for appending.
# 'b' for binary mode.  zoom.exe - binary
# '+' for updating (reading and writing).

# Read and Write content
# Read a File
# Reading Entire Content: content = file_object.read()
# line = file_object.readline() for a single line.
# lines = file_object.readlines() for all lines in a list.

# Close the file


file = open("TestData2.txt", 'r')
content = file.read()
print(content)
file.close()








