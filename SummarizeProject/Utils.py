# @Time    : {2023/5/25} {21:40}
# @Author  : backperker
# @File    : D:\python\PythonProject\SummarizeProject\Utils.py
# @Description : 工具累
import os
from tkinter import filedialog
class Utils:

    def inputStr(self, str):
        inputstr = input(f"{str}\n")
        if inputstr:
            return (inputstr.strip(), True)
        if inputstr:
            return (inputstr.strip(), False)

    def inputInt(self, str):
        inputInt = input(f"{str}\n")
        isdigit = inputInt.strip().isdigit()
        if isdigit:
            return (int(inputInt.strip()), True)
        else:
            print("请输入数字")
            return (inputInt.strip(), False)

    def inputUtils(self, str):
        inp = input(f"{str}\n")
        while not inp:
            inp = input(f"{str}\n")
        return inp

    def isExceptionGET(self, web_driver, url):
        try:
            web_driver.get(url)
            print("正常，执行get请求")
            return False
        except:
            print("异常，执行get请求")
            return True

    def isExceptionRefresh(self, web):
        try:
            web.refresh()
            return False
        except:
            return True

    def selectFiledocumentDialog(self):
        path = filedialog.askopenfilename()
        return path
    def selectFiledocumentDialogWithTitle(self,title):
        path = filedialog.askopenfilename(title=title)
        return path
    def selectFileDialog(self):
        file=filedialog.askdirectory()
        return  file
    def selectFileDialogWithTitle(self,str):
        file=filedialog.askdirectory(title=str)
        return  file
    def check_excel_isOpen(self,filepath):
        # filenames=os.listdir(filepath)
        # try:
        #     for filename in filenames:
        #         os.rename(filepath+"\\"+filename,filepath+"\\tempfile.xls")
        #         os.rename(filepath+"\\tempfile.xls",filepath+"\\"+filename)
        # except OSError:
        #     print("excel 打开状态，请关闭")
        #     return True
        # return False
        try:
            # 未打开
            os.rename(filepath, filepath)
            return False
        except:
            #已打开
            return True

    def isContain(self,str,list:[]):
        if len(list)==0:
            return False
        count = list.count(str)
        if count==0:
            return False
        else:
            return  True