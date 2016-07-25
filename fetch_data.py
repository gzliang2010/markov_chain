import requests
import bs4
import re

def fetch_data(link):
	if re.match(r'http', link) is not None: # test if link is url
		response = requests.get(link)
		soup = bs4.BeautifulSoup(response.text, "lxml")
		web_text = soup.get_text().encode("utf-8")
		print "Load web text successfully!"
		return web_text
	else:
		try:
			my_file = open(link, "r")   #If link is a path of a local file
		except IOError:
			print "Error: Cannot find file!"
			return "" #return empty string. If without anything, it will return None.
		else:
			print "Read file successfully!"
			file_data = my_file.read()
			my_file.close()
			return file_data