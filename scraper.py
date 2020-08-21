from selenium import webdriver
import time
import sys

def playerScraper(player_one, player_two):
    if player_two == player_one:
        sys.exit("Please enter two different players")
    if player_one == "" or player_two == "":
        sys.exit("Please fill in the players' names")

    print("Gathering data...")

    url = "https://www.ultimatetennisstatistics.com/headToHead"

    driver = webdriver.Chrome(
        "/Users/utsavshinghal/Desktop/selenium/webdriver/chrome/chromedriver")

    driver.get(url)

    # submit box for player 1 on the ATP website
    submit_box_one = driver.find_elements_by_tag_name("input")[1]

    # typing the players' names in the search boxes
    for character in player_one:
        submit_box_one.send_keys(character)
        time.sleep(0.3)

    player_lst = driver.find_elements_by_class_name("ui-menu-item")
    player_lst[0].click()

    # submit box for player 2 on the ATP website
    submit_box_two = driver.find_elements_by_tag_name("input")[2]

    for character in player_two:
        submit_box_two.send_keys(character)
        time.sleep(0.3)

    player_lst2 = driver.find_elements_by_class_name("ui-menu-item")
    player_lst2[0].click()

    time.sleep(0.5)

    stats_button = driver.find_element_by_xpath('//*[@id="h2hPills"]/li[6]/a')
    stats_button.click()

    time.sleep(0.5)
    
    stats_button2 = driver.find_element_by_id("statisticsPill")
    stats_button2.click()

    time.sleep(1)

    h2h_button = driver.find_element_by_xpath('/html/body/div[3]/div[7]/div[1]/div[5]/div/label/input')
    h2h_button.click()

    time.sleep(1)

    player_one_pointProb = driver.find_element_by_xpath('/html/body/div[3]/div[7]/div[3]/div[1]/div[1]/table/tbody/tr[24]/th[1]').text
    player_two_pointProb = driver.find_element_by_xpath('/html/body/div[3]/div[7]/div[3]/div[1]/div[1]/table/tbody/tr[24]/th[3]').text

    players = {}
    players[player_one] = player_one_pointProb
    players[player_two] = player_two_pointProb

    return players