import os

#1
def list_directories(path):
    directories = []
    for d in os.listdir(path):
        if os.path.isdir(os.path.join(path,d)):
            directories.append(d)
    return directories

def list_files(path):
    files = []
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            files.append(f)
    return files

def list_all(path):
    all = []
    for f in os.listdir(path):
        all.append(f)
    return all


path = "C:/"

print("\n\tAll:")
print(*list_all(path),sep='\n')

print("\tDirectories:")
print(*list_directories(path),sep='\n')

print("\n\tFiles:")
print(*list_files(path),sep='\n')

#2
def check(path):
    if not os.path.exists(path):
        print("Path does not exist.")
        return
    
    if os.access(path, os.R_OK):
        print("Path is readable.")
    else:
        print("Path is not readable.")
    
    if os.access(path, os.W_OK):
        print("Path is writable.")
    else:
        print("Path is not writable.")
    
    if os.access(path, os.X_OK):
        print("Path is executable.")
    else:
        print("Path is not executable.")

check(path)

#3
def analyze(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print("Path exists.")
        print("Filename:", filename)
        print("Directory:", directory)
    else:
        print("Path does not exist.")

path = input("Input path: ")
analyze(path)

#4
def line_counter(file_n):
    line_count = 0
    with open(file_n,"r") as file:
        for line in file:
            line_count += 1
    print(f"{line_count} line(s) in a text file")

line_counter("4.txt")

#5
def list_to_file(lst):
    with open("5.txt","w") as file:
        for i in lst:
            file.write(str(i) + '\n')

nums = [1,2,3,4,5]
list_to_file(nums)


#6
def many_files():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in alphabet:
        filename = f"{letter}.txt"
        with open(filename, 'w') as file:
            file.write(letter)
        print(f"Created file: {filename}")

many_files()

#7
def copy_content():
    copy_from = "original.txt"
    copy_to = "copied.txt"
    with open(copy_from, "r") as file:
        content = file.read()
    with open(copy_to, "w") as file:
        file.write(content)
    print("content is copied")

copy_content()

#8
def delete(path):
    if os.path.exists(path):
        if os.access(path, os.R_OK):
            os.remove(path)
            print(f"File '{path}' deleted successfully.")
        else:
            print(f"File '{path}' is not accessed.")
    else:
        print(f"File '{path}' does not exist.")

path = "delete.txt"
delete(path)
