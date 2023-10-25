
import requests
from tqdm import tqdm

def downloadMp4(url ,path):
    rep=requests.get(url,stream=path)

    total=int(rep.headers.get('content-length',0))

    with open (path,"wb")as file,tqdm(
        desc=path,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024
    )as bar:
        for data in rep.iter_content(chunk_size=1024):
            size=file.write(data)
            bar.update(size)
    file.close()
    bar.close()
    rep.close()

if __name__=="__main__":
    url="https://vid-cf.xvideos-cdn.com/d63c049758649362536ded58d8f16db7121dd37d-1678727980/videos/mp4/6/e/6/xvideos.com_6e631655ec0962eff1fc4073c52bae56.mp4"
    path=r"E:\ffmeg\video\GangBang sex compilation Vol 18.mp4"
    downloadMp4(url,"18.mp4")