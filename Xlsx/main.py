from selenium import webdriver


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def init():
    s = input("请输入\n")
    print(s)
    if not s:
        init()
    else:
        exit()


if __name__ == '__main__':
    wb = webdriver.Firefox()
    wb.get("https://www.baidu.com/")
