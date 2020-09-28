# from urllib.request import urlopen
import urllib3

from bs4 import BeautifulSoup

http = urllib3.PoolManager()


def Scrape(user):
    # reddit = f"https://www.reddit.com/user/{user}/comments/"
    reddit = http.request(
        'GET', f"https://www.reddit.com/user/{user}/comments/")

    # page = urlopen(reddit)

    soup = BeautifulSoup(reddit.data, features="lxml")

    comments = []
    links = []

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

    return (comments[:10], links[:10])

    # soup.findAll('p')[:-1]
