import requests
import furl

while True:
	inp=input('翻訳したい文字を入力 >>')
	if inp == "quit":
		break
	else:
		url = 'https://script.google.com/macros/s/AKfycbz6YMwrbwy6ZIH2RQCO7YIOENWcykAwfGMNEkyKlu1STj1ZC8pg/exec?text=' + inp + '&source=ja&target=en'
		f = furl.furl(url)
		res = requests.get(f.url)
		print(res.text)