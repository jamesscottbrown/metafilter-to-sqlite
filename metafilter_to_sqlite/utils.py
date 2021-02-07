import sys

import click
import dateparser
import requests
from bs4 import BeautifulSoup


def error(message):
    click.secho(message, bold=True, fg="red")
    sys.exit(-1)

def parse_comments(file, db):
    comments = []
    next_line = "timestamp"

    comment = ""
    with open(file) as fp:
        for line in fp:

            if next_line == "timestamp":
                date = line.strip()
                next_line = "permalink"
                continue

            if next_line == "permalink":
                permalink = line.strip()
                next_line = "comment"
                continue

            if line.strip() == "-----":
                id = int(permalink.split('#')[-1])
                post_url = permalink.split('#')[0]
                subsite = permalink.split('/')[2]

                comments.append(
                    {'id': id, 'date': date, 'url': permalink, 'text': comment, 'subsite': subsite, 'post_url': post_url,})
                comment = ""
                next_line = "timestamp"
                continue

            comment += line.strip()

    db["comments"].insert_all(comments, pk="id", replace=True)

def scrape_posts(user_id, db):
    posts = []
    page = 1
    while True:

        print(f"Loading results page {page}")

        url = f"https://www.metafilter.com/activity/{user_id}/posts/{page}/"
        res = requests.get(url, allow_redirects=False)

        if res.status_code == 404:
            error(f"404 Error encountered trying to load {url}")
            break
        if res.status_code == 301:
            break

        soup = BeautifulSoup(res.content, 'html.parser')


        page += 1

        for post in soup.find_all("h1", class_="posttitle"):
            title = post.text

            url = post.contents[0].attrs['href']
            subsite = url.split("/")[2]
            id = int(url.split("/")[3])

            post_body =  post.find_next_sibling('div')
            text = post_body.prettify()
            text = "".join(text.split("<br/>")[:-1]).strip()

            spans = list(post_body.find('span'))

            date_string  = spans[3].text + " " + spans[4].replace('on', '').strip()
            date = dateparser.parse(date_string)

            favourites = 0
            if len(spans) > 5:
                favourites = int(spans[5].text.replace('(', '').replace(')', '').replace('comments', '').replace('comment', '').strip())

            posts.append({'id': id, 'date': date, 'url': url, 'title': title, 'text': text, 'subsite': subsite, 'num_favourites': favourites, 'user_id': int(user_id)})

    db["posts"].insert_all(posts, pk="id", replace=True)
