#Name:copyfile.py
#Author:Julian Miguel Alapan
#Description:Copy
#Date:August 7, 2020

import shutil

filename=input("Enter the first filename")
file1=open(filename1, 'rb')

filename2=input("Enter the second filename")
file2=open(filename2, 'wb')

shutil.copyfileobj(file1, file2)
