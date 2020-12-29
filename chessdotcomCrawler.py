#!/usr/bin/env python
# coding: utf-8

# # Get pro chess player's games
# chess.com does have an api but those are for games played on their platforms. This class automates getting the games of pro players from this particular page: https://www.chess.com/games. 

# In[1]:



from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import time

class PlayerGames:
    def __init__(self, player):
        self.__player = player #player's name: name-surname
        
        #get the games
        self.__getGames()
        
    def __getGames(self):
        games_url = 'https://www.chess.com/games/' + self.__player
        
        #allow browser to run without gui
        chrome_options = Options()
#         chrome_options.add_argument("--headless")
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(games_url) #go to player's page

        i = 0
        while True:
            #GET THE PLAYER'S GAMES            
            
            #click checkbox
            try:
                driver.execute_script("arguments[0].click();", WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='master-games-check-all']"))))
            except:
                print("If the page says something like: 'Your search did not match any games. Please try a new search' then the player you seek has no games there, otherwise just run the program again")
                
            driver.execute_script("arguments[0].click();", WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='master-games-download-button']"))))
            
            #allows user to let chrome download multiple files
            if i == 1:
                time.sleep(10)
            i += 1

            nextpage_btn = driver.find_element_by_class_name("pagination-next")
            #if there is a next page go to it else we done
            if nextpage_btn.get_attribute("href") != None:
                driver.execute_script("arguments[0].click();", WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "pagination-next"))))
            else:
                print("Done downloading")
                
                time.sleep(5)
                #close browser
                driver.close()
                
                break;        


# ## The Program:
# input: name of chess player(e.g gary-kasparov)
# 
# while running: the driver I am using is chrome which requires you to give you permission to download multiple files. The prompt will only appear on page 2 and after you click allow you don't have to do anything about it.
# 
# output: The download files a saved in your default download path for chrome. 

# In[2]:



name = input("Enter player name(e.g garry-kasparov): ")
games = PlayerGames(name)


# In[ ]:




