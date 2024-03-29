from setuptools import setup

setup(
    author="hritik baweja",
    author_email="bawejahritik@gmail.com",
    description="""A cli tool written in python which mimic linux/unix command wc behaviour.
    more info visit: https://codingchallenges.fyi/challenges/challenge-wc
    """,
    version="0.0.1",
    name="word_count",
    py_modules=["main"],
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "ccwc = main:main",
        ],
    },
)