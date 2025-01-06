from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from parsel import Selector
import urllib
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import os


def scraping(search_query):
    options = webdriver.ChromeOptions() 

    options.add_argument("--disable-gpu")
    options.add_argument('enable-logging')
    options.add_argument("start-maximized")
    options.add_argument("--lang=en_EN")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)
    # actions = ActionChains(driver)

    driver.get(f"https://www.google.com/maps/search/{urllib.parse.quote(search_query)}/")


    #####
    divSideBar=driver.find_element(By.CSS_SELECTOR,f"div[aria-label='Results for {search_query}']")

    keepScrolling=True
    while(keepScrolling):
        divSideBar.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)
        divSideBar.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)
        html =driver.find_element(By.TAG_NAME, "html").get_attribute('outerHTML')
        if(html.find("You've reached the end of the list.")!=-1):
            keepScrolling=False
    #####


    page_content = driver.page_source
    response = Selector(page_content)

    # print(response)
    results = []

    for el in response.xpath('//div[contains(@aria-label, "Results for")]/div/div[./a]'):
    
        # Address
        address = el.xpath('./div[2]/div[4]/div/div/div/div[2]/div[4]/div/span[2]/span[2]/text()').extract_first('')
        if address == '':
            address = el.xpath('./div[2]/div[4]/div/div/div/div[2]/div[4]/div/span[3]/span[2]/text()').extract_first('')
            
        # Split the string and extract the rating and reviews count
        rr = el.xpath('./div[2]/div[4]/div/div/div/div[2]/div[3]/div/span[2]/span/@aria-label').extract_first('')
        if rr!="":
            # Split the string into two parts: rating and reviews
            rating_part, reviews_part = rr.split(" stars ")
            rating = float(rating_part)
            reviews = int(reviews_part.split()[0])  # Extract the first part of the reviews

        results.append({
            'title': el.xpath('./a/@aria-label').extract_first(''),
            'address': address,
            'rating': rating,
            'reviews': reviews,
            'link': el.xpath('./a/@href').extract_first('')
        })

    csv_file_path = 'results/'+search_query+'_data.csv'

    # Check if the file exists and remove it before writing again
    if os.path.exists(csv_file_path):
        os.remove(csv_file_path)

    # Write the data to CSV with pipe delimiter
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "address", "rating", "reviews", "link"], delimiter='|')
        writer.writeheader()
        writer.writerows(results)

    driver.quit()


search_query = input("Enter your keyword: ")
scraping(search_query=search_query)

print("Successfully scraping maps with keyword "+search_query)