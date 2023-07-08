import os
from GoogleImageScrapper.GoogleImageScrapper import GoogleImageScraper

def GoogleImage():
    op = open("C:\\Users\\Gagan\\Desktop\\BlackHole\\Complete NEO series\\Text-Features\\Data.txt",'rt')
    query = str(op.read())
    op.close()
    oc = open("C:\\Users\\Gagan\\Desktop\\BlackHole\\Complete NEO series\\Text-Features\\Data.txt",'r+')
    oc.truncate(0)
    oc.close()

    webdriver = "C:\\Users\\Gagan\\Desktop\\BlackHole\\Complete NEO series\\DataBase\\webdriver\\chromedriver.exe"
    photos = "C:\\Users\\Gagan\\Desktop\\BlackHole\\Complete NEO series\\DataBase\\GooglePhotos\\"

    search_keys = query  
    number = 10
    head = False
    max = (1000,1000)
    min = (0,0)

    for search_key in search_keys:
        image_search = GoogleImageScraper(webdriver,photos,search_keys,number,head,min,max)
        image_url = image_search.find_image_urls()
        image_search.save_images(image_url)

GoogleImage()