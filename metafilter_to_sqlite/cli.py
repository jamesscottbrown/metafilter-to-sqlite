import os
import click
import sqlite_utils

from metafilter_to_sqlite import utils

@click.group()
@click.version_option()
def cli():
    """Save data from MetaFilter to a SQLite database"""

@cli.command()
@click.argument(
    "db_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
@click.option(
    "-f",
    "--file",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    default="my-mefi-comments.txt",
    help="Path to MeFi export file",
)
def comments(db_path, file):
    """Load comments from a downloaded MeFi export file downloaded from http://www.metafilter.com/contribute/my-mefi-export.mefi"""
    db = sqlite_utils.Database(db_path)

    if not os.path.exists(file):
        utils.error(f"File {file} does not exist")

    utils.parse_comments(file, db=db)



@cli.command()
@click.argument(
    "db_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
@click.argument(
    "user_id",
    type=int,
    required=True,
)

def posts(db_path, user_id):
    """Scrape posts for a user from their public profile"""
    db = sqlite_utils.Database(db_path)

    utils.scrape_posts(user_id=user_id, db=db)
