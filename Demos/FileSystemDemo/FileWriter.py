import os.path

# Takes a file and appends poop at the end
def OpenFileAppendPoop(file: str):
    with open(file, 'a+') as writer:
        writer.write('\nPoop')

# Takes a string and creates a file with that name
# If file already exists with that name, append file name with poop
def CreateFileWithName(file: str):
    fileName = file
    while (os.path.exists(fileName)):
        fileName += "poop"

    with open(fileName, 'w+') as writer:
        writer.write('Poop')

    return fileName