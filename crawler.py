import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv

# Use the safari web driver pre installed on mac to get the page in selinium to virtually click on
# the load more button that is javascript with hidden pages.
driver = webdriver.Safari()
# this is the page and at the bottom you see the load more
driver.get('https://rateyourmusic.com/new-music/')
for i in range(10):
    # find the element and click it
    button = driver.find_element_by_id("view_more_new_releases_all").click()
    # short sleep to not overload server
    time.sleep(10)


with open("./input/new_releases.txt", 'w') as f:
    f.write(driver.page_source)


with open("./input/new_releases.txt" , "r") as f:
    soup = BeautifulSoup(f, "lxml")

# The array to use when saving to a file
to_save = []


# Basic info extracts the name of album, name of artist(s), date released
basic_info = soup.find_all('div', class_='newreleases_item_textbox_artistalbum')
basic_info_arr = []

# store all the basic info in the array
for i in basic_info:
    temp = []
    temp.append(i.span.text)
    temp.append(i.a.text)
    temp.append(i.div.text)
    basic_info_arr.append(temp)


stat_info = soup.find_all('div', class_='newreleases_item_statbox')
stat_info_arr = []

# store all the stat box info: avg, rates, wants
for i in stat_info:
    temp = []
    temp.append(i.span.text)
    temp.append(i.span.text)
    temp.append(i.span.text)
    stat_info_arr.append(temp)

# Organize and save all the info for saving inside the to_save array
for i in range(len(basic_info_arr)):
    temp = []
    for j in range(3):
        temp.append(basic_info_arr[i][j])
    for j in range(3):
        temp.append(stat_info_arr[i][j])
    to_save.append(temp)

# Save the results as a csv file to the ouputs
with open('./output/new_releases.csv', 'a+') as f:
    writer = csv.writer(f)

    for i in to_save:
        writer.writerow(i)

print("Data gathered from the website was successfully saved to outputs")