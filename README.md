# metafilter-to-sqlite

Save your user activity from [Metafilter](https://www.metafilter.com/) to a SQLite database.

## Installation

Clone this repository, then run `python setup.py install`.


## Usage

### Loading imported comments

If you are logged in, then you can download a file containing your comments [here](http://www.metafilter.com/contribute/my-mefi-export.mefi).
Note that you are only able to do this once per week.

You can then process this file using the command:

    $ metafilter-to-sqlite comments  -f /path/to/my-mefi-comments.txt metafilter.db

### Scraping posts

You can scrape posts from a MetaFilter user profile using the command:

    $ metafilter-to-sqlite posts metafilter.db <user_id>

where `<user_id>` is the numerical id (not username) of an account.

## Limitations

This can only import comments and posts that you have made; it does not save comments or posts by other users that you have favourited.

This information could be obtained by web-scraping in the future.
