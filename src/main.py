from FrequencySummariser import FrequencySummarizer
import urllib2
from bs4 import BeautifulSoup

import nltk
nltk.download('punkt')

def get_only_text(url):
	""" 
	 return the title and the text of the article
	 at the specified url
	"""
	page = urllib2.urlopen(url).read().decode('utf8')
	soup = BeautifulSoup(page, "html.parser")
	text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
	return soup.title.text, text
	
feed_xml = urllib2.urlopen('http://feeds.bbci.co.uk/news/rss.xml').read()
feed = BeautifulSoup(feed_xml.decode('utf8'))
to_summarize = map(lambda p: p.text, feed.find_all('guid'))



fs = FrequencySummarizer()
for article_url in to_summarize[:5]:
  title, text = get_only_text(article_url)
  print '----------------------------------'
  print title
  for s in fs.summarize(text, 2):
   print '*',s