from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
data=list()
stream =['arts','science','commerce','management','agriculture','engineering','computer-applications','education','medical','vocational-courses','law','mass-communications','design','paramedical','hotel-management','animation','architecture','pharmacy','aviation','dental']

for i in range(0,len(stream)):
  # site= "https://www.indcareer.com/find/all-colleges-in-himachal%2Bpradesh?page="+str(i)
  site=  'https://collegedunia.com/'+stream[i]+'/arunachal-pradesh-colleges'
  hdr = {'User-Agent': 'Mozilla/5.0'}
  req = Request(site,headers=hdr)
  page = urlopen(req)

  soup = BeautifulSoup(page, "html.parser")
  # print(soup)
  # Retrieve all of the h4 tags that contain college name inside anchor tag
  tags = soup('div')
  for tag in tags:
    try:
        # Retrieve all of the a tags that contain college name inside title tag
      data.append(tag.find('a').find('h3').contents[0])
      
    except:
      print("An exception occurred")  


df = pd.DataFrame(data)

df.to_csv('list.csv', index=False)
