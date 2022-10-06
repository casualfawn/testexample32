from django.shortcuts import render
from django.http import HttpResponse
import requests

#keywords = ['crypto', 'stock', 'wall street', 'finance', 'investing']

#url = 'https://newsapi.org/v2/everything?q=stock, invest, finance, wallstreet&from=2022-04-15&sortBy=popularity&apiKey=aa70d972e63b47d28ab25a921a82635f'
url = 'https://newsapi.org/v2/everything'
params = {'q': 'stock AND Nvidia',
           #'sortBy': 'popularity',
                'apiKey': 'aa70d972e63b47d28ab25a921a82635f'
               }

crypto_news = requests.get(url, params=params).json()
crypto_news

def index(request):
    
    	
    a = crypto_news['articles']
    desc =[]
    title =[]
    img =[]
    
    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        mylist = zip(title, desc, img)

    context = {'mylist': mylist}
    return render(request, 'Newsapp/index.html', context)

# Create your views here.
