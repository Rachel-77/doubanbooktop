import requests
from requests.exceptions import RequestException
import re 
import csv
import time
    
    
def get_page(url):
    headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
    try:
        re = requests.get(url=url,headers=headers)
        if re.status_code == 200:
            return re.text
        return None
    except RequestException:
        return None

def get_inform(html):
    rex = '.*?class="pl2">.*?a.*?title="(.*?)".*?pl">(.*?)</p>.*?nums">(.*?)</span>.*?'
    pattern = re.compile(rex,re.S)
    items = re.findall(pattern,html)
    
    for item in items:
        content = item[1]
        num = 0
        for i in content:
            if i =='/':
                num+=1
       

        if num ==3:
            au=content.split('/')[0]
            i = content.split('/')[1]
            deta=content.split('/')[2]
            trs = ''
        

        elif num ==4 or num == 5:
            au=content.split('/')[0]
            i=content.split('/')[2]
            deta=content.split('/')[3]
            trs=content.split('/')[1]
        
        elif num==2:
            trs = ''
            au= ''
            i=content.split('/')[0]
            deta=content.split('/')[1]

        # print(i)
        # print(deta)
        # print(trs)
        dict={
            'name':item[0],
            'author' : au,
            'trs':trs,
            'publisher':i,
            'publishdate' :deta,
            'score':item[-1] 
        }
        print(dict)
        csv_write.writerow(dict)
        
if __name__=='__main__':
    # url = 'https://book.douban.com/top250?start=100'
    # html = get_page(url)
    # get_inform(html)
    fb = open('tushutop.csv','a',encoding='utf-8',newline='')
   
    csv_write=csv.DictWriter(fb,fieldnames=['name','author','trs','publisher','publishdate','score'])
    csv_write.writeheader()
    urls = ['https://book.douban.com/top250?start={}'.format (str(ii)) for ii in range(0,226,25)]
    for url in urls:
        html = get_page(url)
        get_inform(html)
        time.sleep(2)
    fb.close()
