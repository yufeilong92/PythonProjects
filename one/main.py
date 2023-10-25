import os
import tkinter

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook

import DataVo
from JAV_Web import JAV_Web
from ReadAndCopyXlsx import ReadAndCopyXlsx
from TxtUtils import TxtUtils
from tkinter import filedialog
import tkinter as tk

from Utils import Utils

if __name__ == '__main__':
   rc= ReadAndCopyXlsx()
   rc.initInput()
