# quoters
A pythonic random quote generator with multiple categoties.

[![codecov.io](https://codecov.io/github/suman-kr/quoters/coverage.svg?branch=master)](https://codecov.io/github/suman-kr/quoters?branch=master)
> Installation
```sh
pip install quoters
```

> Running and usage
```py
from quoters import Quote
print(Quote.print())
```
> Linux shell configuration (BASH)
```sh
git clone --branch master https://github.com/suman-kr/quoters.git && cd quoters
chmod +x quoters_script.py
ln -s <PATH_TO_GIT_REPO>/quoters_script.py /usr/local/bin/quoters

### Add the below line to your .bashrc. 
export PATH=$PATH:/usr/local/bin 
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
