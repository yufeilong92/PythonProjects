
from  selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

if __name__ == '__main__':

    driver=webdriver.Firefox()
    driver.get("D:\python\PythonProject\one\oni.html")
    print("===========")

    plants = driver.find_elements(By.TAG_NAME, "li")
    print(plants)

    print("===========")