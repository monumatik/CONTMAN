import requests
from .analyze import analyzeWebsiteContent

def makeRequest(url):
	try: 
		response = analyzeWebsiteContent(requests.get(url).content)
	except requests.exceptions.MissingSchema:
		response = ['Missing schema URL']
	except requests.exceptions.ConnectionError:
		response = ['Connection error to URL']
	except requests.exceptions.InvalidURL:
		response = ['Invalid URL']
	except Exception as ex:
		response = ['Unexpected error']
		print(ex)
	return response

