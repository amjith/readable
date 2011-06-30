import subprocess
import urllib2
import readability
from html2text import html2text

def retrive_page(url):
    return urllib2.urlopen(url).read()

def main():
    #url = "http://johnpaulett.com/2009/10/15/html-to-restructured-text-in-python-using-pandoc/"
    url = "http://antirez.com/post/take-advantage-of-redis-adding-it-to-your-stack.html"
    html = retrive_page(url)
    readable_html = readability.Document(html).summary()
    text = html2text(readable_html)
    print text

if __name__ == '__main__':
    main()
