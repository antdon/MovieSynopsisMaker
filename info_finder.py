from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import pdb
#TODO - try catch for neterror

class InfoFind():
    def __init__(self, title: str) -> None:
        self.options = webdriver.FirefoxOptions()
        self.options.headless = True
        self.driver = webdriver.Firefox(options=self.options)
        self.title = title

    def GetInfo(self) -> str:
        ind: int = 0
        potential_synop_xpath = ['/html/body/div[3]/div[3]/div[5]/div[1]/p[2]','/html/body/div[3]/div[3]/div[5]/div[1]/p[4]']
        self.driver.get("https://www.wikipedia.org/")
        self.driver.find_element_by_name('search').send_keys(self.title)
        self.driver.find_element_by_xpath('/html/body/div[3]/form/fieldset/button').click()
        try:
            self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[4]/div[3]/ul/li[1]/div[1]/a').click()
        except NoSuchElementException:
            self.driver.find_element_by_xpath('//*[@id="mw-search-DYM-suggestion"]').click()
            self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[4]/div[3]/ul/li[1]/div[1]/a').click()
        synop = self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[5]/div[1]/p[2]')
#       if synop.text == '':
#           synop = self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[5]/div[1]/p[4]')
        while synop.text == '' and ind != len(potential_synop_xpath) - 1:
            synop = self.driver.find_element_by_xpath(potential_synop_xpath[ind])
            ind += 1
        if synop.text == '':
            synop = "could not find synopsis" 
        if  isinstance(synop, str):
            return synop
        else:
            return synop.text


