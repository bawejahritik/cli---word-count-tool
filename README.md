# ccwc - Your Fun Word Count Tool! 📊

## Introduction

Welcome to py_wc, your own version of the Unix command line tool wc, built with Python and the click library. This tool follows the Unix philosophies, providing simple parts connected by clean interfaces and designed to be easily connected to other programs.

This challenge is a part of the coding challenges given by John Crickett: https://codingchallenges.fyi/challenges/intro

Challenge Link: https://codingchallenges.fyi/challenges/challenge-wc

## Prerequisites

- **Python Version:** 3.11.5
- **CLI Library:** click

## Setup

1. Clone the repository: `git clone <repo link>`
2. Navigate to the project directory: `cd WORD_COUNT`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate`
5. Install required packages: `python3 -m pip install --editable .`

## Features

ccwc provides the following counts:

- **Word Count:** `-w` or `--words`
- **Line Count:** `-l` or `--lines`
- **Character Count:** `-m` or `--chars`
- **Byte Count:** `-c` or `--bytes`

## How to Use

1. Activate the virtual environment if not already activated: `source venv/bin/activate`
2. Run the command: `py_wc <option> <file1>`
3. Use stdin with pipes: `cat filename | ccwc -<option>`

## Sample Command

```bash
ccwc -wlc test.txt
```

## Enjoy Exploring with py_wc! 🚀

Feel free to experiment, connect it with other tools, and explore the power of simplicity in software engineering. If you have any questions or suggestions, don't hesitate to reach out. Happy coding! 🎉