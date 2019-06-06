from bs4 import BeautifulSoup
from re import findall

def analyzeWebsiteContent(websiteContent):
	soup = BeautifulSoup(websiteContent, 'html.parser')
	meta_keywords = soup.head.find('meta', attrs={'name':'keywords'})
	if meta_keywords is None:
		return ['No keywords']
	else:
		content = meta_keywords['content']
		words = content.split(",")
		result = []
		for word in words:
			find = findall(str(word.lower()), str(soup.body))
			result.append(str(word.lower()) + ' - ' + str(len(find)))

		return result