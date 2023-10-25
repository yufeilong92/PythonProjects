import os.path
import time

from Utils import Utils
from DataVo import DataVo


class TxtUtils:
    def creataTxt(self):
        u = Utils()
        vo = DataVo()
        print("请选择TXT文件，其他文件报错")
        time.sleep(1)
        path = u.selectFiledocumentDialog()
        content=u.inputUtils(vo.PLEASE_INPUT_CONTENT)
        if os.path.exists(path):
            print(f"{path}文本已经存在了，追加")
            open_a = open(path, "a")
        else:
            print(f"{path}文本不存在，创建")
            open_a = open(path, "w")
        open_a.write(content)

        open_a.close()