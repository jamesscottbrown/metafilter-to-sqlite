# metafilter-to-sqlite

Save your user activity from [Metafilter](https://www.metafilter.com/) to a SQLite database.

## Installation

    $ pip install metafilter-to-sqlite

## Downloading your comments

If you are logged in, then you can download a file containing your comments [here](http://www.metafilter.com/contribute/my-mefi-export.mefi).
Note that you are only able to do this once per week.

You can then process this file using the command:

    $ metafilter-to-sqlite -f /path/to/my-mefi-comments.txt metafilter.db

## Limitations

This only saves **comments** (not **posts**) that you have made; it does not save comments or posts by other users that you have favourited.

This information could be obtained by web-scraping in the future.
