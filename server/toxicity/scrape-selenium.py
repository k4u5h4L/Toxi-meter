import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup


def scrape_comments(user):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--window-size=1920x1080")

    browser = webdriver.Chrome(chrome_options=chrome_options)
    # browser = webdriver.Chrome()

    browser.get(f"https://www.reddit.com/user/{user}/comments/")
    time.sleep(1)

    elem = browser.find_element_by_tag_name("body")

    no_of_pagedowns = 20

    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        no_of_pagedowns -= 1

    soup = BeautifulSoup(browser.page_source, features="lxml")

    browser.quit()

    comments = []
    links = []

    print(soup.findAll("h3"))

    if len(soup.findAll("h3")) == 0:
        return (0, 0)
    elif soup.findAll("h3")[0].text == "Sorry, nobody on Reddit goes by that name.The person may have been banned or the username is incorrect.":
        return (0, 0)
    else:
        for comment in soup.findAll("p")[:-1]:
            comments.append(comment.text)

        for i in soup.findAll("h3"):
            parent_element = i.parent.parent
            # print('https://reddit.com' + str(parent_element.get('href')))
            links.append('https://reddit.com' +
                         str(parent_element.get('href')))

    return (comments[:45], links[:45])
