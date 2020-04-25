from django.shortcuts import render
from newsapi import  NewsApiClient
from textblob import TextBlob
from datetime import datetime,timedelta
from . import imagextraction


today = datetime.utcnow().date()
duration = datetime.utcnow().date() - timedelta(days = 15)


def index(request):
    news = NewsApiClient(api_key = "0de6787ea7e44a8691ce4a5d556d18dc")
    top_headlines = news.get_everything(q='covid OR corona OR success OR recovered OR lockdown OR quarantine OR recovery',
                                      from_param=duration,
                                      language='en')
    l=top_headlines['articles']
    newsfeed = []
    desc =[] 
    news =[] 
    img =[] 
    for i in range(len(l)):
        f=l[i]
        article = TextBlob(f['description'])
        if(article.sentiment.polarity > 0.2):
            t = imagextraction.imgextract(f['title'][:20])
            news.append(f['title'])   
            desc.append(f['description'])
            img.append(str(t))
    newsfeed=zip(news,desc,img)     
    #return newsfeed
    #newsfeed = sentiment(top_headlines,0.2)

    return render(request, 'index.html', context ={"newsfeed":newsfeed})
    
                                      
