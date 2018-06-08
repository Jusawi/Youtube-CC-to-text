import re
import sys
from bs4 import BeautifulSoup
import urllib.request

""" A few HTML encodings replacements
&amp;#39; to '
&amp;quot; to "
"""


def scrapper(url):
    response = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(response, "lxml")
    s = re.sub(r'<.+?>', '', soup.prettify())
    s = re.sub(r'\n', '', s)
    s = re.sub('\s+', ' ', s).strip()
    return s


def main(argv):
    """ argv[1] for language and argv[2] for video link """
    URL = "http://video.google.com/timedtext?lang=" + \
        argv[1] + "&v=" + argv[2]
    cc = scrapper(URL)
    fp = open("subs.txt", 'w')
    fp.write(cc)
    fp.close()


if __name__ == "__main__":
    main(sys.argv)
