import requests
from bs4 import BeautifulSoup as bs
import os

#source
url = '' # the source you want the bot take images from

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

image0 = 0 #img name

#get images
for image in image_loc:
  try:
    url = image['src']
    source = requests.get(url)
    if source.status_code == 200:
      with open('img-' + str(image0) + '.jpg', 'png') as mkimg:
        mkimg.write(requests.get(url).content)
        mkimg.close()
        image0 += 1
  except:
    pass
