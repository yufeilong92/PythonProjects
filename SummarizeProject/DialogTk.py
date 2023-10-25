#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/29 20:04
# @Author  : backpacker
# @File    : DialogTk.py
# @Description : 提示框

from tkinter import *
from tkinter import messagebox, Scrollbar

from CopyFiles import CopyFiles
from ReadAndCreate import ReadAndCreate


class DialogTk:

    def showInlet(self):
        print()
        root = Tk()
        # root.geometry("640x540")
        root.title("界面展示")
        root.config(bg="snow")

        Label(root, text="选择操作", background="CornflowerBlue", font=18, width=40).grid(row=0, column=1, columnspan=2,
                                                                                          sticky=W + E)
        val = IntVar(master=root)
        Radiobutton(root, text="拷贝目录生产数据", font=14, selectcolor="green", background="gray", variable=val,
                    indicatoron=False, value=0).grid(row=2, column=1, columnspan=2, pady=4, sticky=W + E)
        Radiobutton(root, text="选择本地xlsx,追加或创建xlsx", font=14, variable=val, selectcolor="green",
                    background="gray", indicatoron=False, value=1).grid(row=3, column=1, pady=4, columnspan=2,
                                                                        sticky=W + E)

        button = Button(root, text="确认", font=18, command=lambda: self.inletSure(val))
        button.grid(row=5, column=1, columnspan=2, pady=8, sticky=W + E)

        mainloop()

    def inletSure(self, vaL: IntVar):
        index = vaL.get()
        if index == 0:
            copyFile = CopyFiles()
            copyFile.selectDialog()
        elif index == 1:
            readCreate = ReadAndCreate()
            readCreate.readFileAndData()

    # copyfinle=CopyFiles()
    # copyfinle.selectDialog()
    # mai=ReadAndCreate()
    # mai.readFileAndData()
    # print("你好")
    # print_hi('PyCharm')
    # root=Tk()
    # root.geometry("600x450")
    # root.title("请选择操作")
    # label=Label(root,text="签名",fg="red")
    # label.grid()
    # entry = Entry(root, takefocus="请输入内容")
    # entry.grid(row=0,column=1)
    #
    # btn=Button(root,text="确认",command=lambda :print_hi("a"))
    # btn.grid(row=0,column=2)
    #
    # root.mainloop()
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/

    # master = Tk()
    # master.geometry("640x540")
    # # Tkinter string variable
    # # able to store any string value
    # v = StringVar(master, "1")
    # master.config(bg="light gray")
    # # Dictionary to create multiple buttons
    # values = {"RadioButton 1": "1", "RadioButton 2": "2", "RadioButton 3": "3", "RadioButton 4": "4",
    #           "RadioButton 5": "5"}
    #
    # # Loop is used to create multiple Radiobuttons
    # # rather than creating each button separately
    # for (text, value) in values.items():
    #     radiobutton = Radiobutton(master, text=text, variable=v, value=value, selectcolor="light green", indicator=0, background="light blue",
    #                               command=lambda: print_hi(v))
    #     radiobutton.pack(fill=X,
    #                      ipady=5)
    #
    # # Infinite loop can be terminated by
    # # keyboard or mouse interrupt
    # # or by any predefined function (destroy())
    # mainloop()

    # root = Tk()
    # root.geometry("640x540")
    # root.title("创建xlsx")
    # root.config(bg="light gray")
    # labal = Label(root, text="表名", font="18")
    # labal.grid(row=0, column=1,columnspan=1,sticky=E+W)
    #
    # edit = Entry(root, font="18")
    # edit.grid(row=0, column=2,columnspan=1,sticky=E+W)
    #
    # labal_Path = Label(root, text="请选择地址", font="18")
    # labal_Path.grid(row=1, column=1,columnspan=1,sticky=E+W)
    # btn = Button(root, text="选择地址", font="18",command=lambda :selectFile(labal_Path))
    # btn.grid(row=1, column=2,columnspan=1,sticky=E+W)
    # btnsure = Button(root, text="创建", font="18",command=lambda :sure(edit))
    # btnsure.grid(row=2, column=1,columnspan=2,sticky=E+W)
    #
    # root.mainloop()
    # 原始按钮布局
    # b_login = Button(root, text='登录', command=reg)
    # b_login.grid(row=3, column=1, sticky=W, pady=10)
    # b_cancel = Button(root, text='取消', command=root.quit)
    # b_cancel.grid(row=3, column=1)
    # root = Tk()
    # root.title("请登录")
    # # 登录结果 提示
    # l_msg = Label(root, text='')
    # l_msg.grid(row=0, columnspan=2)  # 跨越两列显示
    #
    # # 第一行用户名输入框
    # l_user = Label(root, text='用户名：')
    # l_user.grid(row=1, sticky=W)
    # e_user = Entry(root)
    # e_user.grid(row=1, column=1, sticky=E, padx=3)
    #
    # # 第二行密码输入框
    # l_pwd = Label(root, text='密码：')
    # l_pwd.grid(row=2, sticky=E)
    # e_pwd = Entry(root)
    # e_pwd['show'] = '*'  # 隐藏显示
    # e_pwd.grid(row=2, column=1, sticky=E, padx=3)
    #
    # # 第三行登录按钮
    # f_btn = Frame(root)
    # b_login =Button(f_btn, text='登录', width=6)
    # b_login.grid(row=0, column=0)
    # b_cancel =Button(f_btn, text='取消', width=6)
    # b_cancel.grid(row=0, column=1)
    # f_btn.grid(row=3, columnspan=2, pady=10)
    # root.mainloop()
    #     messagebox.showwarning("警告", "当前操作失败！")
    #     messagebox.showinfo("提示", "当前操作成功！")
    #     messagebox.showerror("错误", "程序出现异常，请稍后再试！")
    #     if messagebox.askquestion("询问", "是否要删除该文件？") == 'yes':
    #         # 用户点击了“是”按钮，执行删除操作
    #         print("是")
    #     else:
    #         print("否")
    #         # 用户点击了“否”按钮，取消操作
    #     if messagebox.askokcancel("询问", "确定要关闭该窗口吗？"):
    #         print("确定")
    #     # 用户选择了“确定”，执行关闭窗口操作
    #     else:
    #         print("取消")
    # # 用户选择了“取消”，继续执行操作
    #     if messagebox.askyesno("询问", "当前操作可能影响系统稳定性，确定要继续吗？"):
    #         print("是")
    #     # 用户选择了“是”，继续执行操作
    #     else:
    #         print("否")
    #     # 用户选择了“否”，取消操作
    def add(self, lb: Text):
        lb.insert(END, "asdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasd")
        lb.see("end")

    def textDialog(self):
        root = Tk()
        root.geometry("640x540")
        root.title("标题数据")

        Label(root, text="展示数据", font=10).pack(side=LEFT, fill=Y)
        sb = Scrollbar(root)
        lb = Listbox(root, yscrollcommand=sb.set)

        button = Button(root, text="添加数据", font=10, command=lambda: self.add(lb))
        button.pack(side=LEFT, fill=Y)

        lb.pack(side=LEFT)
        sb.pack(side=RIGHT, fill=Y)
        sb.config(command=lb.yview())

        mainloop()

    def textDialogGrid(self):
        root = Tk()
        root.title("标题数据")

        Label(root, text="展示数据", font=10).grid(row=0, column=0, columnspan=2, sticky=W + E)
        text = Text(root)
        scrollbar = Scrollbar(orient=VERTICAL,command=text.yview())

        scrollbar.config(command=text.yview)
        text.config(yscrollcommand=scrollbar.set)

        button = Button(root, text="添加数据", font=10, command=lambda: self.add(text))
        button.grid(row=100, column=0, sticky=W + E, columnspan=2)

        text.grid(row=1, column=0, columnspan=2, sticky=W + E)
        scrollbar.grid(row=1,column=2,sticky=N+S)

        mainloop()
