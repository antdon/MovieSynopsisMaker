from selenium import webdriver
import time

class InfoFind():
    def __init__(self, title: str) -> None:
        self.driver = webdriver.Firefox()
        self.title = title

    def GetInfo(self) -> str:
        self.driver.get("https://www.wikipedia.org/")
        search_bar = self.driver.find_element_by_name('search')
        search_bar.send_keys(self.title)
        search_but = self.driver.find_element_by_xpath('/html/body/div[3]/form/fieldset/button')
        search_but.click()
        result = self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[4]/div[3]/ul/li[1]/div[1]/a')
        result.click()
        synop = self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[5]/div[1]/p[2]')
        return synop.text

poop = InfoFind("10 things I hate about you movie")
poop.GetInfo()

