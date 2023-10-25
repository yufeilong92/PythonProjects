#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/24 22:22
# @Author  : 我的名字
# @File    : YellowProject.py
# @Description : $
import time
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
import openpyxl


def saveYellow(savePath, saveName, url, whileNum):
    postionItem = 1
    baseUrl = url
    itemIndex = 1
    baseItemHear = "https://z2212k.xyz/pw/"

    if os.access(savePath, os.W_OK):
        print(f'{savePath}文件已经存在')
    else:
        open(savePath, "a+")
    writer = pd.ExcelWriter(savePath, mode="a")
    timeData = time.strftime("%H-%M-%S", time.localtime())
    data = []
    # for num in range(0, 10):
    #     data.insert(num,(f'值{num}',f'值2{num}'))
    while postionItem < whileNum:
        url = f'{baseUrl}&page={postionItem}'
        print(url)
        print("开始请求数据")
        req = requests.get(url)
        req.encoding = "utf-8"
        rep = BeautifulSoup(req.text, "html.parser")
        find_all = rep.findAll("h3", class_="")
        # print(find_all)
        for item in find_all:
            saveWeb = baseItemHear + item.find('a')['href']
            saveWebName = item.getText()
            data.insert(itemIndex, (f'{saveWebName}', f'{saveWeb}'))
            itemIndex += 1
        # time.sleep(1)
        postionItem += 1
    else:
        print("faild")

    pdf = pd.DataFrame(data, columns=['名称', '地址'])
    pdf.index.name = '序号'
    pdf.to_excel(writer, f'{saveName}{timeData}', False)
    writer.close()
    print("保存成功")


if __name__ == '__main__':
    savePath = "D:\python\yellow.xlsx"
    saveName = "三集写真"
    # url = "https://z2212k.xyz/pw/thread1022.php?fid=219"
    # url = "https://z2212k.xyz/pw/thread1022.php?fid=5"
    # url = "https://z2212k.xyz/pw/thread1022.php?fid=3"
    url = "https://z2212k.xyz/pw/thread1022.php?fid=18"
    whileNum = 163
    saveYellow(savePath, saveName, url, whileNum)
