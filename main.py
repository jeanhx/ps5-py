import webbrowser
from requests_html import HTMLSession
import json

# Uncomment to track disc
code = "playstation5-console.3005816"

# Uncomment to track digital
# code = "playstation5-digital-edition-console.3005817"

product_url = "https://direct.playstation.com/en-us/consoles/console/%s" % code

found = False
count = 0
tries = 0

user_agent = {'User-agent': 'Mozilla/5.0'}

# generate new session and render
session = HTMLSession()

while not found and tries <5:
	try:

		count += 1
		r = session.get(product_url, headers=user_agent)
		# print(r.html.html)
		print("==========================================================================")
		print("Searching site for queue-it, take %s" % count)
		r.html.render(sleep=1)
		if len(r.html.find('.softblock')):
			continue
		elif len(r.html.find('#queue-it_log')):
			print("==========================================================================")
			print("Found queue on direct site, opening browser")
			found = True
			webbrowser.open(product_url, new=1)
		tries = 0

	except:
		print("==========================================================================")
		print("Puppeteer failed, retrying")
		session = HTMLSession()
		tries += 1
