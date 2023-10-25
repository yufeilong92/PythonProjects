# This is a sample Python script.
import os
import tkinter.simpledialog
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Notebook
# import tkinter as tk
from CopyFiles import CopyFiles
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# from tkinter import *
# from tkinter import  messagebox
# def print_hi(name):
#
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi,{name}')  # Press Ctrl+F8 to toggle the breakpoint.
#     print(f'Hi,{name.get()}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# def  sure(edit):
#     title = edit.get().title().strip()
#     print(f"{title}")
#
# def selectFile(labar:Label):
#     labar["text"]="asdads"
from ReadAndCreate import ReadAndCreate
from Utils import Utils
# Press the green button in the gutter to run the script.
from  DialogTk import DialogTk
if __name__ == '__main__':
   # dialog=DialogTk()
   # dialog.showInlet()
   # copyfinle=CopyFiles()
   # copyfinle.selectDialog()
   # mai=ReadAndCreate()
   # mai.readFileAndData()
   td=DialogTk()
   td.textDialogGrid()

