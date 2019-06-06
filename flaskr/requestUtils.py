import requests
from .analyze import analyzeWebsiteContent

def makeRequest(url):
	try: 
		response = analyzeWebsiteContent(requests.get(url).content)
	except requests.exceptions.MissingSchema:
		response = ['Wrong URL']
	except requests.exceptions.ConnectionError:
		response = ['Connection error to URL']
	except:
		response = ['Unexpected error']
	return response

