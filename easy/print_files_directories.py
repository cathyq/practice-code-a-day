# Print out all the files from the path, whether the files are in directories or not.

# METHOD 1 
for i in listdir(sPath):
    if isdir(join(sPath, i)):
        for k in listdir(join(sPath,i)):
            print k
    else:
        print i

# METHOD 2 (recursive)
def print_directory_contents(sPath):
    for i in listdir(sPath):
        cPath = join(sPath, i)
        if isdir(cPath):
            print_directory_contents(cPath)
        else:
            print i

print_directory_contents(path)