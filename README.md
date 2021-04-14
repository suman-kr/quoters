# quoters
A python web scrapper to generate random quote

> Installation
```sh
pip install quoters
```

> Running and usage
```sh
from quoters import Quote
print(Quote.print())
```
## Contents
> Available Functions
```py
print() # Returns random quotes
print_series_quote() # Returns random TV shows quotes
print_anime_quote() # Returns random Anime quotes
```
> Offline usage example
```py
print(True)
```
`Note: Pass True as a parameter for fallback. It works for all the available functions.`

## Resources
The data consumed are from the following sources:
- https://www.yourselfquotes.com/thought-of-the-day/
- https://www.tvtime.com/article/top-50-unforgettable-tv-quotes
- https://bayart.org/anime-quotes/

## API
The package can also be used from API. API is hosted on [Heroku](https://www.heroku.com/)
```
http://py-quoters.herokuapp.com/ [Random quote]
http://py-quoters.herokuapp.com/?query=series [Random TV Shows quote]
http://py-quoters.herokuapp.com/?query=anime [Random Anime characters quote]
```
### Thanks! :heart:
