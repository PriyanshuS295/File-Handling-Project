from pathlib import Path
import os

def readfileandfolder():
    path=Path('')
    items=list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")


def createfile():
    try:
        readfileandfolder()
        name=input("Write the name of your file which you want to create: ")
        p=Path(name)
        if not p.exists():
            fs=open(p,'w')
            data=input("give the data what you want to write: ")
            fs.write(data)
            print("File created and Data entered successfully")

        else:
            print("This file already exists")

    except Exception as err:
        print(f"An error occured as {err}")

def readfile():
    try:
        readfileandfolder()
        name=input("Name the file which you want to read: ")
        p=Path(name)
        if p.exists() and p.is_file():
            fs=open(name)
            p=fs.read()
            print(p)

        else:
            print("The file does not exist")
    
    except Exception as err:
        print(f"An error occured as {err}")

def updatefile():
    try:
        readfileandfolder()
        name=input("Name the file which you want to update: ")
        p=Path(name)
        if p.exists() and p.is_file():

            print("Enter 1 to update the name of file.")
            print("Enter 2 to overwrite data in the file.")
            print("Enter 3 to append data in the file.")

            choice=int(input("Enter what you want to update: "))

            if choice==1:
                upname=input("Write the new name of file: ")
                p2=Path(upname)
                p.rename(p2)

  
            if choice==2:
                fs=open(name,'w')
                data=input("Write the data what you want to overwrite: ")
                fs.write(data)
                print("Data overwritten successfully")


            if choice==3:
                fs=open(name,'a')
                data=input("Write the data what you want to append: ")
                fs.write(" "+data)
                print("Data appended successfully")

        else:
            print("File does not exists")

    except Exception as err:
        print(f"An error occured as {err}")


def deletefile():
    try:
        readfileandfolder()
        name=input("Name the file which you want to delete: ")
        p=Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("File Deleted Successfully")

        else:
            print("File does not exists")


    except Exception as err:
        print(f"An error occured as {err}")


print("Enter 1 for creating file")
print("Enter 2 for reading file")
print("Enter 3 for updating file")
print("Enter 4 for deleting file")

option=int(input("Enter what you want to do: "))

if option==1:
    createfile()

if option==2:
    readfile()

if option==3:
    updatefile()

if option==4:
    deletefile()



