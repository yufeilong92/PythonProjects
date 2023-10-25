#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/27 18:28
# @Author  : backpacker
# @File    : Dialog.py
# @Description :定义对话框
from abc import abstractmethod, ABCMeta
from  tkinter import *

class DialogSHow(metaclass=ABCMeta):
    @abstractmethod
    def sure(self):
        raise NotImplemented

    @abstractmethod
    def cancel(self):
        raise NotImplemented
def appendXlsx(data):
    print("aaa")
    AppendData(False,data)
def createNewXlsx(data):
    print("create")
    AppendData(False,data)


def AppendData(isShowDialog:bool,data:[]):
    if bool:
        root=Tk()
        root.title("请选择操作流程")
        var =IntVar()
        var.set(0)
        root.geometry("650x450")
        radiobutton = Radiobutton(root, text="选择已有的xlsx,追加数据",font="18",variable=var,value=1,command=lambda :appendXlsx(data))
        radiobutton.grid(row=1,column=1)
        createbutton = Radiobutton(root, text="创建新的xlsx,并保存",font="18", variable=var,value=2,command=lambda :createNewXlsx(data))
        createbutton.grid(row=2,column=1)
        root.mainloop()
