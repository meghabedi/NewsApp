from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.

def index(request):
    newsapi = NewsApiClient(api_key = '**put_your_api_key**')
    top_headlines = newsapi.get_everything(sources='techcrunch',language = 'en')
    #sources = newsapi.get_sources()
    items = top_headlines['articles']
    title = []
    des = []
    img = []

    for i in range(len(items)):
        l = items[i]
        title.append(l['title'])
        des.append(l['description'])
        img.append(l['urlToImage'])
    news_item = zip(title,des,img)

    return render(request,'index.html',{'news_item':news_item})


