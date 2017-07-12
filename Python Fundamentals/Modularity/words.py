"""Retrieve and print words from a file
Usage:
    python words.py <URL>
"""

x = 3

from urllib.request import urlopen
import sys

#http://sixty-north.com/c/t.txt


def fetch_words(url):
    """ Fetch a list of words from a URL.

      Args:
          url: The URL of a UTF-8 text document

      Returns:
          A list of strings containing the words

      """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                x = word
                story_words.append(word)
        return story_words


def print_items(items):
    """Prints one item per line

    :param items:
        list: can be a list of anything
    :return:
        Nothing
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from a URL

    Args:
        url: a URL of a UTF-8 text doc
    """
    words = fetch_words(url)
    print_items(words)




print(__name__)
if __name__ == '__main__':
    # main(sys.argv[1])
    with urlopen(sys.argv[1]) as data:
        for text in data:
            print(text.decode('utf-8').strip())
