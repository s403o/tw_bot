import requests
from bs4 import BeautifulSoup as bs
import os

#source
url = '' 

#down page 
page = requests.get(url)
html = bs(page.text, 'html.parser')

#locate
image_loc = html.findAll('img')

#create folder for located imgs
if not os.path.exists('imgs'):
  os.makedirs('imgs')

#open the new folder
os.chdir('imgs')

x = 0 #img name

#get images
for image in image_loc:
  try:
    url = image['src']
    source = requests.get(url)
    if source.status_code == 200:
      with open('img-' + str(x) + '.jpg', 'png') as mkimg:
        mkimg.write(requests.get(url).content)
        mkimg.close()
        x += 1
  except:
    pass