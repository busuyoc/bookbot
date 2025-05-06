# BookBot

BookBot is a Python command-line tool that analyzes text files to count words and calculate character frequency.

## Features

- Count the total number of words in a text file
- Count the frequency of each alphabetical character (case-insensitive)
- Display character frequencies in descending order
- Works with UTF-8 encoded text files

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/bookbot.git
   cd bookbot
   ```

## Usage

Run BookBot from the command line by providing the path to a book in the pre-configured books directory:

```bash
python main.py ./books/[book_filename].txt
```

The available books are:
- `frankenstein.txt` - Mary Shelley's Frankenstein
- `pride_and_prejudice.txt` - Jane Austen's Pride and Prejudice 
- `moby_dick.txt` - Herman Melville's Moby Dick

For example:

```bash
python main.py ./books/frankenstein.txt
```

Note: The `books/` directory is included in `.gitignore` and not tracked in the repository. You'll need to add these book files to this directory before running the program.

If you don't provide a file path, the program will show usage instructions.

## Example Output

```
============ BOOKBOT ============
Analyzing book found at ./books/frankenstein.txt...
----------- Word Count ----------
Found 78057 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
o: 25225
i: 24613
n: 24367
s: 21155
r: 20818
h: 19725
l: 14583
d: 14331
...
============= END ===============
```

## Project Structure

- `main.py`: Entry point for the program
- `stats.py`: Contains functions for text analysis
  - `count_words()`: Counts total words in text
  - `count_chars()`: Counts alphabetical character frequency
  - `sort_dictionary()`: Sorts character counts in descending order

## Customization

You can modify the character counting to include non-alphabetical characters by changing the condition in the `count_chars()` function in `stats.py`.
