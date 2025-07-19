#!/usr/bin/python3
#Date 16/08/2022
#Tool title "ia-binder"
#Description "Tool used to bind image and archive file together"
#Compatible with Windows OS only 
#Made by @esistdini

import os

op = os.name

def cls():
    
    if op == 'nt':
        os.system("cls")
    else:
        os.system("clear")
        print("Your OS is not compatible")
        exit()

def create():

    cls()
    
    imgn = input("Enter the image name : ") #Enter the image file name
    
    afn = input("Enter the rar/zip file name : " ) #Enter the rar file name
    #If you haven't made it yet , create one
    
    nofn = input("Enter the output name with image extention : " ) #output name

    os.system("copy /b " + imgn + "+" + afn + " " + nofn) #Command

    fs = os.path.getsize(nofn) #Gets the file size

    print("New file size is : " , fs , " Bytes") #Display file size


def read():

    cls()

    fn = input("Enter the file name : " ) #Enter the image name

    ofn = input("Enter the output file name : " ) #New output rar file name

    ofn = ofn.replace(" " , "") #Replace space

    os.system("ren " + fn + " " + ofn + ".rar") #Command

def main():
    print("1 - Create a new image")
    print("2 - Read the image")
    usr_input = int(input("Choose a option : " ))
    if usr_input == 1:
        create()
    elif usr_input == 2:
        read()
    else:
        print("Not available")
        exit()

        

main()
