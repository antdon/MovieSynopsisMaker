from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import pdb
import sys
#TODO - try catch for neterror

class InfoFind():
    """
    Class containing functions relating to the creation of synopsis. 
    Searchs wikipedia for title of movie and creates the string object of the first 
    paragraph
    Parameters:
        title - name of movie
    """
    def __init__(self, title: str) -> None:
        self.options = webdriver.FirefoxOptions()
        self.options.headless = True
        self.driver = webdriver.Firefox(options=self.options)
        self.title = title

    def GetInfo(self) -> str:
        """
        Navigates from wikipedia home page to the page relating to the movie and
        returns the first paragraph of that page
        Return:
            The first paragraph of the movie's wikipedia page
        """
        ind: int = 0
        #List containing the potential xcodes for the paragraph
        potential_synop_xpath = ['/html/body/div[3]/div[3]/div[5]/div[1]/p[2]','/html/body/div[3]/div[3]/div[5]/div[1]/p[4]']
        self.driver.get("https://www.wikipedia.org/")
        self.driver.find_element_by_name('search').send_keys(self.title)
        self.driver.find_element_by_xpath('/html/body/div[3]/form/fieldset/button').click()
        #try catch to account for "did you mean" page
        try:
            self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[4]/div[3]/ul/li[1]/div[1]/a').click()
        except NoSuchElementException:
            self.driver.find_element_by_xpath('//*[@id="mw-search-DYM-suggestion"]').click()
            self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[4]/div[3]/ul/li[1]/div[1]/a').click()
        synop = self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[5]/div[1]/p[2]')
        #while loop to iterate through possible synop xpaths
        while synop.text == '' and ind != len(potential_synop_xpath) - 1:
            synop = self.driver.find_element_by_xpath(potential_synop_xpath[ind])
            ind += 1
        #checks if synop is still empty and handels error
        if synop.text == '':
            #if error is encountered change synop into string error message
            synop = "could not find synopsis" 
            print("could not find synopsis for " + self.title, file = sys.stderr) 
        #since method returns a string, if synop is of type string synop itself
        #can be returned 
        if  isinstance(synop, str):
            return synop
        else:
            return synop.text


