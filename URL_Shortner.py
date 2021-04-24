import pyshorteners

def shortner(link):
	short = pyshorteners.Shortner()
	short_link = short.tinyurl.short(link)
	return short_link

url = input('Enter URL : ')

final = shortner(url)

print(f"Shortened Link is {final}")