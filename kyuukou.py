#!pip3 install requests
#!pip3 install beautifulsoup4
#!pip3 install chardet
#!pip3 install schedule

import requests
from bs4 import BeautifulSoup
import schedule
import time

prev = 'a'

def dailyjob():
  site = requests.get('http://kyoumu.office.uec.ac.jp/kyuukou/kyuukou.html')
  soup = BeautifulSoup(site.content,'html.parser')    #Countermeasures against garbled text
  caninfo = soup.find('p').text   #information of cancel  
  #########ここにbotがチャンネルに書き込むためのプログラムを書く。変数はcaninfo#########

def minjob():
  ite = requests.get('http://kyoumu.office.uec.ac.jp/kyuukou/kyuukou.html')
  soup = BeautifulSoup(site.content,'html.parser')    #Countermeasures against garbled text
  caninfo = soup.find('p').text   #information of cancel 
  
  if prev != caninfo:
    #########ここにbotがチャンネルに書き込むためのプログラムを書く。変数はcaninfo#########
    prev = caninfo

def main():
  #Everyday
  schedule.every().day.at("20:00").do(dailyjob)

  #Every10min
  schedule.every(1).second.do(minjob)
