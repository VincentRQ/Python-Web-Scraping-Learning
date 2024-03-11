import requests as r

url = "https://en.wikipedia.org/wiki/Rare-earth_element"
resp = r.get(url)

resp.status_code

resp.text


from selectolax.parser import HTMLParser
tree = HTMLParser(resp.text)

type(tree)
tree.css("p")
type(tree.css("p"))