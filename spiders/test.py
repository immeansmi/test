from selenium import webdriver
import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
import re


class Accountdata:

    def __init__(self, zipcode=10004, url = 'https://www.wellsfargo.com/savings-cds/rates/'):
        self.zipcode = zipcode
        self.url = url
        self.driver = webdriver.Firefox()
        print("Opening Web")
        self.driver.get(self.url)
        sleep(3)
        self.login()



    def login(self):
        zipcode_input = self.driver.find_element_by_xpath('//*[@id="zipCode"]')
        zipcode_input.send_keys(self.zipcode)
        continue_btn = self.driver.find_element_by_xpath('//*[@id="c28lastFocusable"]')
        continue_btn.click()

    def datable(self):
        html_source = self.driver.page_source
        df = pd.read_html(html_source)
        return df




if __name__ == '__main__':
    app = Accountdata()
    sleep(5)
    df = app.datable()
