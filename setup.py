import os

from setuptools import setup

VERSION = "0.1"

def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="metafilter-to-sqlite",
    description="Save data from MEtafilter to a SQLite database",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="James Scott-Brown",
    author_email="james@jamesscottbrown.com",
    url="https://github.com/jamesscottbrown/metafilter-to-sqlite",
    project_urls={
        "Source": "https://github.com/jamesscottbrown/metafilter-to-sqlite",
        "Issues": "https://github.com/jamesscottbrown/metafilter-to-sqlite/issues",
    },
    classifiers=[],
    keywords="metafilter sqlite export dogsheep",
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["metafilter_to_sqlite"],
    entry_points="""
        [console_scripts]
        metafilter-to-sqlite=metafilter_to_sqlite.cli:cli
    """,
    install_requires=[
        "click",
        "sqlite-utils~=2.4.4",
    ],
    extras_require={"test": ["pytest"]},
    tests_require=["metafilter-to-sqlite[test]"],
)