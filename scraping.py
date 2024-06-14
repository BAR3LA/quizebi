from bs4 import BeautifulSoup
import requests
import csv
import time
from random import randint



pg = 1 

my_file = open('quiz4.csv','w',encoding='utf-8_sig',newline='\n')
file_obj = csv.writer(my_file)
file_obj.writerow(['სათაური','ფასი','წიგნის სურათის ლინკი'])

while pg< 16:

    url = f'https://biblusi.ge/products?category=291&page={pg}'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    results = soup.find('div',class_='row')
    all_books = results.find_all('div',class_='mb-1_875rem col-sm-4 col-md-3 col-xl-2 col-6')


    for book in all_books:
        saxeli = book.find('acronym').text.strip()
        fasi = book.find('div',class_='text-primary font-weight-700').text.strip().replace(' ','').strip()[:-2] +" ₾"
        linki = book.find('div',class_='b-aspect d-flex bg-white __aspect').get('style')[22:-3]
        file_obj.writerow([saxeli,fasi,linki])

    pg += 1
    
    time.sleep(randint(15,20))
    

my_file.close()






