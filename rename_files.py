import os
import string

def rename_files():
    translation = str.maketrans(string.ascii_letters, string.ascii_letters, string.digits)
    ar = os.listdir("G:\learning\prank\prank")
    os.chdir("G:\learning\prank\prank")
    for filename in ar:
        #print(filename)
        temp = filename.translate(translation)
        os.rename(filename, temp)
        print(temp)
rename_files()
