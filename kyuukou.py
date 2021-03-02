!pip3 install requests
!pip3 install beautifulsoup4
!pip3 install chardet
!pip3 install schedule

import requests
from bs4 import BeautifulSoup
import schedule
import time

prev = 'a'

def dailyjob():
  site = requests.get('http://kyoumu.office.uec.ac.jp/kyuukou/kyuukou.html')
  soup = BeautifulSoup(site.content,'html.parser')    #Countermeasures against garbled text
  Allcaninfo = soup.find('p').text   #information of cancel
  Splitcaninfo = Allcaninfo.split("\n")
  for caninfo in Splitcaninfo:
    if "現在、休講の予定はありません。" in caninfo :
      #########ここにbotがチャンネルに書き込むためのプログラムを書く。変数はcaninfo#########
    elif "月" in caninfo:
      #########ここにbotがチャンネルに書き込むためのプログラムを書く。変数はAllcaninfo#########
      break

def minjob():
  site = requests.get('http://kyoumu.office.uec.ac.jp/kyuukou/kyuukou.html')
  soup = BeautifulSoup(site.content,'html.parser')    #Countermeasures against garbled text
  Allcaninfo = soup.find('p').text   #information of cancel
  
  if prev != Allcaninfo:
      Splitcaninfo = Allcaninfo.split("\n")
    for caninfo in Splitcaninfo:
      if "現在、休講の予定はありません。" in caninfo :
        #########ここにbotがチャンネルに書き込むためのプログラムを書く。変数はcaninfo#########
      elif "月" in caninfo:
        #########ここにbotがチャンネルに書き込むためのプログラムを書く。変数はAllcaninfo#########
        break

def main():
  #Everyday
  schedule.every().day.at("20:00").do(dailyjob)

  #Every10min
  schedule.every(10).minutes.do(minjob)