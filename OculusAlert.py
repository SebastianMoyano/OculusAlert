#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Mar 13 22:40:35 2020

@author: sebastianmoyano
"""

import requests
from bs4 import BeautifulSoup
import  smtplib
import os,sys
import schedule
import time




def get_script_directory():
    path = os.path.realpath(sys.argv[0])
    if os.path.isdir(path):
        return path
    else:
        return os.path.dirname(path)
def sendmsm():
    try:
        with open(os.path.join(get_script_directory(),'credential.txt'),'r') as f:
                text=f.read().split(',')
                
        email=text[0]
        password=text[1] 
        content=''
        r=requests.get('https://www.oculus.com/quest/')
        soup= BeautifulSoup(r.text,'html.parser')
        s=soup.findAll('div',{'class','_7_5p'})
        for x in s:
            if "Not Available" not in x.text:
                lista=os.listdir(get_script_directory())
                if "finish.no" not in lista:     
                    print("Disponible, creando")
                    with open(os.path.join(get_script_directory(),"finish.no"),'w') as file:
                        file.write("dont delete,this is limiting the amount of msj")
                content += "Available Now!!!!!! "+ x.text
                print("Available Now!!! "+ x.text)
                mail = smtplib.SMTP('smtp.gmail.com',587)
                mail.ehlo()
                mail.starttls()
                mail.login(email,password)
                mail.sendmail(email, email, content.encode("utf8"))
           
              
            else:
                lista=os.listdir(get_script_directory())
                if "finish.no" in lista:     
                    print("Agotado, borrando")
                    os.remove(os.path.join(get_script_directory(),"finish.no"))

                print("Aun agotado " + x.text)
    except Exception as e:
            print(e) 
  
schedule.every(1).minutes.do(sendmsm)

while True:
    schedule.run_pending()
    time.sleep(5)


    