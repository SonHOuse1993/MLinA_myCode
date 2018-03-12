import feedparser
ny=feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
ny['entries']
print len(ny['entries'])
