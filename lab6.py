import os
import glob

filesInUse = []
root = os.getcwd()


def createFile():
    filename = input("Enter a filename: ")
    file = open(filename, "w")
    filesInUse.append(filename)
    content = input("Enter the content of the file: ")
    file.write(content)
    print(filesInUse)


def deleteFile(filename):
    print(filesInUse)
    if filename not in filesInUse:
        print(filename)
        os.remove(filename)
    else:
        print("File is in use, cannot be deleted!!!")


def makeDirectory():
    directoryName = input("Enter the name of the directory: ")
    directoryName = root + "/" + directoryName
    os.mkdir(directoryName)


def changeDirectory():
    directoryName = input(
        "Enter the name of the directory you want to go to: ")
    directoryName = root + "/" + directoryName
    if os.path.isdir(directoryName):
        os.chdir(directoryName)
    else:
        print("Directory does not exist!!!")


def moveFile():
    filename = input("Enter the name of the file you want to move: ")
    directoryName = input(
        "Enter the name of the directory you want to move the file to: ")
    directoryName = root + "/" + directoryName
    if os.path.isdir(directoryName):
        os.rename(filename, directoryName + "/" + filename)
    else:
        print("Directory does not exist!!!")


def openFile():
    filename = input("Enter the name of the file you want to open: ")
    mode = input(
        "Enter the mode you want to open the file in:\n w for write_at\n a for append\n")
    match mode:
        case 'w':
            startingIndex = input("Enter starting index: ")
            file = open(filename, "r")
            filesInUse.append(file)
            userContent = input("Enter the content you want to add: ")
            contents = file.read()
            filesInUse.remove(file)
            file.close()
            contents = str(contents)

            if int(startingIndex) > len(contents):
                startingIndex = len(contents)

            contents = contents[:int(startingIndex)] + \
                userContent + contents[int(startingIndex):]
            file = open(filename, "w")
            filesInUse.append(file)
            file.write(contents)

        case 'a':
            filename = open(filename, "a")
            filesInUse.append(filename)
            content = input("Enter the content to append: ")
            filename.write(content)

        case 'r':
            filename = open(filename, "r")
            filesInUse.append(filename)
            print(filename.read())

        case 'x':
            # index = input("Enter ending index: ")
            file = open(filename, "r")
            filesInUse.append(file)
            # print(str(file[0]))))
            # print(str(file[1]))))
            print(file[0])
            # print(file[:index])

        case _:
            print("Invalid mode!!!")


def moveWithinFile():
    filename = input("Enter the name of the file you want to write to: ")
    file = open(filename, "r")
    filesInUse.append(file)
    contents = file.read()
    filesInUse.remove(file)
    file.close()
    contents = str(contents)
    moveDataFrom = int(input("Enter starting index: "))
    moveDataTo = int(input("Enter ending index: "))
    lengthOfDataToMove = int(input("Enter length of data to move:"))
    dataToMove = contents[moveDataFrom:moveDataFrom + lengthOfDataToMove]
    contents = contents[:moveDataFrom] + \
        contents[moveDataFrom + lengthOfDataToMove:]
    contents = contents[:moveDataTo] + dataToMove + \
        contents[moveDataTo:]

    file = open(filename, "w")
    filesInUse.append(file)
    file.write(contents)
    filesInUse.remove(file)
    file.close()


def truncateFile():
    size = input("Enter new size:")
    filename = input("Enter the name of the file you want to truncate: ")
    fileSize = os.path.getsize(filename)
    if int(size) < fileSize:
        file = open(filename, "r+")
        filesInUse.append(file)
        file.truncate(int(size))
        filesInUse.remove(file)
        file.close()
    else:
        print("File is already smaller than the size you want to truncate to!!!")


def closeFile():
    filename = input("Enter the name of the file you want to close: ")
    if filename in filesInUse:
        filesInUse.remove(filename)
        filename.close()
    else:
        print("File is not opened")


def memoryMap():
    # obj = os.scandir()
    # for entry in obj:
    #     if entry.is_file():
    #         print(entry.name)
    #     else:
    #         print(entry.name)
    for file in glob.iglob(root, recursive=True):
        print(file)


if __name__ == "__main__":
    while True:
        print("Welcome to the file system")
        print("1. Create a file")
        print("2. Delete a file")
        print("3. Close file")

        mode = input("Enter the mode you want to run the file system in: ")
        match mode:
            case '1':
                createFile()
            case '2':
                filename = input(
                    "Enter the name of the file you want to delete: ")
                deleteFile(filename)
            case '3':
                closeFile()
            case '4':
                memoryMap()
            # case '5':
            #     changeDirectory()
            # case '6':
            #     moveFile()
            # case '7':
            #     openFile()
            # case '8':
            #     moveWithinFile()
            # case '9':
            #     truncateFile()
            case '0':
                print("exiting")
                break
            case _:
                print("Invalid mode!!!")

    print("Thank you for using the file system")
