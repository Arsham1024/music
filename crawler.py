from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
import pandas as pd
import numpy as np

def crawler(num_pages):
    # wait before loading a new page
    sleep_secs = 5
    # The array to use when saving to a file
    to_save = []

    # Use the safari web driver pre installed on mac to get the page in selinium to virtually click on
    # the load more button that is javascript with hidden pages.
    driver = webdriver.Safari()

    # this is the page and at the bottom you see the load more
    driver.get('https://rateyourmusic.com/new-music/')
    for i in range(num_pages):
        # find the element and click it
        button = driver.find_element_by_id("view_more_new_releases_all").click()
        # short sleep to not overload server
        time.sleep(sleep_secs)

    # download the loaded pages and write the html source code to the input file
    with open("./input/new_releases.txt", 'w') as f:
        f.write(driver.page_source)

    # use the input file to parse the data in lxml
    with open("./input/new_releases.txt" , "r") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Extract basic information
    basic_info_arr = get_basic_info(soup)
    # Extract the stats
    stat_info_arr = get_stat_info(soup)

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
            # implement a check for duplicates
            writer.writerow(i)
    # Output is successful
    print("Data gathered from the website was successfully saved to outputs")

#     Turn into pandas
    df = turn_into_pandas(to_save)
    return df

# Extract the basic information of the song from the parsed html downloaded
# info to extract : Song name, Artist's name, Album name, Date released.
def get_basic_info(soup):
    basic_info = soup.find_all('div', class_='newreleases_item_textbox_artistalbum')
    basic_info_arr = []
    # store all the basic info in the array
    for i in basic_info:
        temp = []
        temp.append(i.span.text)
        temp.append(i.a.text)
        temp.append(i.div.text)
        basic_info_arr.append(temp)
    return basic_info_arr

# Extract the stats of a particular entry.
# info to extract: Ratings, Wants, Avg
def get_stat_info(soup):
    stat_info = soup.find_all('div', class_='newreleases_item_statbox')
    stat_info_arr = []
    # store all the stat box info: avg, rates, wants
    for i in stat_info:
        temp = []
        # need to specify the exact span because this div has 3 spans in it.
        temp.append(i.find('span', class_="newreleases_stat newreleases_avg_rating_stat").text)
        temp.append(i.find('span', class_="newreleases_stat newreleases_ratings_stat").text)
        temp.append(i.find('span', class_="newreleases_stat newreleases_wishlist_stat").text)
        stat_info_arr.append(temp)
    return stat_info_arr

# For better categorization turn into pandas
def turn_into_pandas(arr):
    cols = ["Artist Name" , "Song/Album Name", "Date Released", "Avg Rate" , "Number of People Rated" , "Wants"]
    df = pd.DataFrame(arr, columns=cols)

    # Correcting the style of data frame
    df.style.set_properties(**{'arr-align': 'left'})
    return df

# Run main
if __name__ == "__main__":
    # Run the crawler
    # The number of pages we need to crawl for this website. each pages has 25 entries
    num_pages = 1

    # Run the crawler for this number of pages
    print(crawler(num_pages))
