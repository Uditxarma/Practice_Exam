'''Code to check existence of path that return true or false'''

#Method1
import os
path_1 = "Sample file"
if os.path.exists(path_1):
    print("Exist path: {path_1}")


#Method2
from pathlib import Path
path_2 = Path("Sample file")

if path_2.exists():
    print("Exist path: {path_2}")



#Method3(Check seperatly for file or directory)
path_3a = "Sample file"
path_3b = "Sample file/UditCTC.pdf"

if os.path.isdir(path_3a):
    print("Directory Exists")
else:
    print("Not a directory")


if os.path.isfile(path_3b):
    print("File Exists")
else:
    print("File Doesn't exist")



#Method4(Using try catch)
path_4 = "Sample file/UditCTC.pdf"
try:
    with open(path_4,'r') as f:
        print("File exist confirmed")
except FileNotFoundError:
    print("File doesn't found")
except Exception as e:
    print(str(e))


'''
Linux Command to check path exist or not
#Method(Check if a file or directory exists)
if [ -e "Sample file"]; then
    echo "Path exists"
else
    echo "Path doesn't exist"
fi


Here change accordingly
[ -f "Sample file"]      #Check if it's specifically a file
[ -d "Sample file"]      #Check if it's specifically a directory
[ -e "Sample file"] && echo "Exists || echo "Does not Exists"                 #One-liner (handy for scripts) 

'''




###################################################################################################################################################

'''finding the full path of files inside a folder in string form'''
#Method1
folder = Path("Sample file")
for file in folder.iterdir():
    print(file)                             #file = folder + file
    if file.is_file():
        print("Exist")
    
    print(file.resolve())                   #.resolve() gives the absolute path.


#Method2
folder2 = "Sample file"
for filename in os.listdir(folder2):
    print(filename)                         #filename with extension
    full_path = os.path.join(folder2,filename)
    print(full_path)
    if os.path.isfile(full_path):
        print("File Exist")
        print(os.path.abspath(full_path))          #for full absolute path
    else:
        print("Does not Exist")



#Method3(Using glob(pattern matching))
import glob
for file in glob.glob("Sample file/*"):
    print(file)
    print(os.path.abspath(file))


"""
Linux
#Method1
find "Sample file" -type f -name "myfile.txt"       #single file
find "Sample file" -type f                          #Lists all files with full absolute paths.
realpath "Sample file/myfile.txt"                   #for a known file
readlink -f "Sample file/myfile.txt"

"""

############################################################################################################################################################
'''string splitting'''
print("string splitting")

text = "Hello World . New York, USA"

#Method1(Standard splitting)
print(text.split(","))                  #split from left, default separator = whitespace (" ").

#Method2(Right-side splitting)
print(text.rsplit(".", 1))              #split from right, Useful when you only want the last part of a string (e.g., filename extension).

#Method3(Split by newline)              #Perfect for reading files or multi-line strings.
text = "line1\nline2\nline3"
print(text.splitlines())

#Method4(Split into 3 parts)
data = "user:password"
print(data.partition(":"))                 #Always returns a tuple of 3 parts: (before, separator, after), Great when you only need the first occurrence of a separator

#Method5(Split into 3 parts from right)
filename = "report.final.pdf"
print(filename.rpartition("."))

#Method6(Regex-based splitting (advanced))
import re
texte = "apple, banana; orange|grape"
print(re.split(r"[,;|]\s*", texte))         #Super powerful for splitting with multiple separators.

