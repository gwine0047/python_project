from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

# website to scrape
website = "https://www.thesun.co.uk/sport/football/"

# setting up chrome extension
path = r"C:\Users\FashN\OneDrive\Desktop\CODES\python_project\chromedriver.exe"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

# getting a set of divs by their class and setting them into a container list
containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

titles = []
# subtitles = []
links = []

# iterating over the containers
for container in containers:
    # container = //div[@class="teaser__copy-container"] which is represented by the .
    # Use find_element instead of find_elements to get a single element
    title = container.find_element(by="xpath", value='./a/h3').text
    # subtitle = container.find_element(by="xpath", value='./a/p').text
    link = container.find_element(by="xpath", value='./a').get_attribute("href")

    titles.append(title)
    # subtitles.append(subtitle)
    links.append(link)

# Creating a dictionary
my_dict = {
    'title': titles,
    # 'subtitle': subtitles,
    'link': links
}

# Creating a DataFrame
df_headline = pd.DataFrame(my_dict)

# Saving to CSV
df_headline.to_csv('headline.csv', index=False)

# Closing the webdriver
driver.quit()
