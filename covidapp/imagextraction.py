import requests
from bs4 import BeautifulSoup

def imgextract(search):
    try:
        params = {"q": search}
        r = requests.get("http://www.bing.com/images/search", params=params)

        soup = BeautifulSoup(r.text, "html.parser")
        links = soup.find("a", {"class": "thumb"})

        #print(links.attrs["href"])

        return links.attrs["href"]

    except Exception:
        return "https://miro.medium.com/max/5000/1*Q33vwKNBXPxeOpmg9WPsrw.jpeg"
  