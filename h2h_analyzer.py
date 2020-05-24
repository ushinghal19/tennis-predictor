from selenium import webdriver
import time
import sys

player_one = input("Enter player 1's name (Ex: 'Rafael Nadal') here: ")
player_two = input("Enter player 2's name (Ex: 'Novak Djokovic') here: ")

if player_two == player_one:
    sys.exit("Please enter two different players")
if player_one == "" or player_two == "":
    sys.exit("Please fill in the players' names")

url = "https://www.atptour.com/en/players/atp-head-2-head/" \
      "roger-federer-vs-andreas-seppi/F324/SA93"

driver = webdriver.Chrome(
    "/Users/utsavshinghal/Desktop/selenium/webdriver/chrome/chromedriver")

driver.get(url)

submit_boxes = driver.find_elements_by_class_name("head-to-head-search-input")

# submit box for player 1 on the ATP website
submit_box_one = submit_boxes[0]

# submit box for player 2 on the ATP website
submit_box_two = submit_boxes[1]

# typing the players' names in the search boxes
for character in player_one:
    submit_box_one.send_keys(character)
    time.sleep(0.3)

for character in player_two:
    submit_box_two.send_keys(character)
    time.sleep(0.3)

# getting their ATP code, ie: Rafael Nadal: N406
results = driver.find_elements_by_class_name("head-to-head-search-result")

if len(results) != 2:
    sys.exit("Please spell the players' names correctly")

player_one_id = results[0].get_attribute("data-value")
player_two_id = results[1].get_attribute("data-value")

# breaking the players' names into first name and last name
p1_parsed = player_one.split(" ")
p1_first = p1_parsed[0]
p1_second = p1_parsed[1]

p2_parsed = player_two.split(" ")
p2_first = p2_parsed[0]
p2_second = p2_parsed[1]

# visiting the website where their head-to-head stats are
driver.get("https://www.atptour.com/en/players/atp-head-2-head/"
           "{}-{}-vs-{}-{}/{}/{}".format(p1_first, p1_second, p2_first,
                                         p2_second, player_one_id,
                                         player_two_id))
previous_matches = driver.find_elements_by_css_selector(
    ".modal-event-breakdown-scores [href]")

links = []
stats = []
p1_percentage = 0
p2_percentage = 0
matches = 0

# creating a list of all the links that store previous match data
for match in previous_matches:
    link = match.get_attribute('href')
    links.append(link)

# running through links and seeing their points won percentage in each match
for link in links:
    driver.get(link)
    elements = driver.find_elements_by_class_name("match-stats-number-left")
    for element in elements:
        value = element.text[:2]
        stats.append(value)
    winner = driver.find_element_by_class_name("first-name").text
    if p1_first.lower() == winner.lower():
        p1_temp = int(stats[-1])
        p1_percentage += p1_temp
    else:
        p1_temp = 100 - int(stats[-1])
        p1_percentage += p1_temp
    matches += 1
    p2_temp = 100 - p1_temp
    print("match #{}: {}'s point percentage: {}, {}'s point percentage: {}" \
          .format(matches, player_one, p1_temp, player_two, p2_temp))
    print()

p1 = p1_percentage / matches  # Point percentage of p1
print("{}'s point percentage is {}".format(player_one, p1))
p2 = 100 - p1  # Point perentage of p2
print("{}'s point percentage is {}".format(player_two, p2))
