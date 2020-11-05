''' from www.practicepython.org
completed on 03.11.2020

Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
'''
__author__: 'maxisui'

import requests
from bs4 import BeautifulSoup

url = 'http://www.reasonabledeviations.com/'
r = requests.get(url)

soup = BeautifulSoup(r.text, features="html.parser")

for story_heading in soup.find_all(class_=["post-title"]):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.a.contents[0].strip())