from django.shortcuts import render

import requests


def getdata(request):
	response = requests.get('https://meme-api.herokuapp.com/gimme').json()
	context = {
		'url': response['url']
	}

	return render(request, 'index.html', context)
