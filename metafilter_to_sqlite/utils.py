import sys

import click


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
                id = permalink.split('#')[-1]
                subsite = permalink.split('/')[2]

                comments.append(
                    {'date': date, 'permalink': permalink, 'comment': comment, 'id': id, 'subsite': subsite})
                comment = ""
                next_line = "timestamp"
                continue

            comment += line.strip()

    db["comments"].insert_all(comments, pk="perm", replace=True)
    return comments
