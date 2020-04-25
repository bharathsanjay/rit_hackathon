# Covid News Portal

A Web based Application that gathers positive news article content from the internet based on Sentiment Analyis and real-time Covid-19
statistics.   

## Technology Stack
### Frontend
HTML, CSS - Page Layout

Bootstrap - Page Responsiveness

Javascript - Interactivity

### Backend
Python v3.8

NewsAPI for Python - Extracting news articles in JSON Format from news sources worldwide.

TextBlob - A Python based Naive Bayes classifier library for text sentiment analysis 

BeautifulSoup - Web Scrapping 


## Usage

To use the News Analysis module seperately in your python file,   

```python
import news
area = "Chennai"
news.newsfeed(area) # Returns news feed for a specific area in JSON format
news.sentiment(area,value) # Returns sentiment analysed newsfeed
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
