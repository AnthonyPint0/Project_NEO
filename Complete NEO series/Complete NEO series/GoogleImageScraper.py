import scrapy
import os
import requests
from PIL import Image


class GoogleImageScraper(scrapy.Spider):
    name = "image_scraper"

    def __init__(self, search_key="cat", number_of_images=1, min_resolution=(0, 0), max_resolution=(1920, 1080), *args, **kwargs):
        super(GoogleImageScraper, self).__init__(*args, **kwargs)
        # Check parameter types
        if (type(number_of_images) != int):
            print("GoogleImageScraper Error: Number of images must be integer value.")
            return
        self.search_key = search_key
        self.number_of_images = number_of_images
        self.min_resolution = min_resolution
        self.max_resolution = max_resolution
        self.saved_extension = "jpg"

    def start_requests(self):
        url = "https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947".format(
            self.search_key)
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        image_urls = response.css('img.rg_i::attr(src)').getall()
        count = 0
        for image_url in image_urls:
            if (count >= self.number_of_images):
                break

            if(image_url[:4].lower() not in ["http"]):
                continue

            filename = "{}{}.{}".format(self.search_key, str(count), self.saved_extension)
            image_path = os.path.join("images", filename)
            print("{} .Image saved at: {}".format(count, image_path))

            try:
                response = requests.get(image_url)
                if response.status_code == 200:
                    with open(image_path, 'wb') as f:
                        f.write(response.content)
                    with Image.open(image_path) as img:
                        image_resolution = img.size
                        if (not self.min_resolution[0] <= image_resolution[0] <= self.max_resolution[0]) or (
                                not self.min_resolution[1] <= image_resolution[1] <= self.max_resolution[1]):
                            os.remove(image_path)
                            print("[!] Image removed due to resolution requirements not met.")

                count += 1
            except Exception as e:
                print("GoogleImageScraper Error: Failed to be downloaded.", e)
                pass

        print("Download Completed. Please note that some photos may not have been downloaded due to format or resolution requirements not being met.")