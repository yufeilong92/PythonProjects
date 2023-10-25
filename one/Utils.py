
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
    def selectFileDialog(self):
        file=filedialog.askdirectory()
        return  file
