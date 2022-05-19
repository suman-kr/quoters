# quoters
A pythonic random quote generator with multiple categoties. (Python 3)

[![codecov.io](https://codecov.io/github/suman-kr/quoters/coverage.svg?branch=master)](https://codecov.io/github/suman-kr/quoters?branch=master) [![Pypi Downloads](https://pepy.tech/badge/quoters/month)](https://pepy.tech/project/quoters) [![npm version](https://badge.fury.io/js/quoters.svg)](https://badge.fury.io/js/quoters)

## PyPi

> Installation
```sh
pip install quoters
```

> Running and usage
```py
from quoters import Quote
print(Quote.print())
```

> Available Functions
```py
print() # Returns random quotes
print_series_quote() # Returns random TV shows quotes
print_anime_quote() # Returns random Anime quotes
print_programming_quote() # Returns random Programming quotes
```
> Offline usage example
```py
print(True)
```
`Note: Pass True as a parameter for fallback. It works for all the available functions.`

## NPM


> Installation

```sh
npm install quoters
```

> Running and usage

```js
// ES6 and Typescript
import Quote from 'quoters';
const randomQuote = new Quote('QUOTE').get()
console.log(randomQuote);

// ES5 and old JS
var Quote = require('quoters').default;
const randomQuote = new Quote('QUOTE').get()
console.log(randomQuote);
```

> Categories
```
- QUOTE: Random quote
- ANIME: Random anime quote
- SERIES: Random famous TV series quote
- PROGRAMMING: Random geeky quote xD
```

## CLI

> BASH / ZSH shell configuration (Linux and MacOS)
```sh
git clone --branch master https://github.com/suman-kr/quoters.git && cd quoters
chmod +x quoters_script.py
pip install -r requirements.txt
ln -s <ABSOLUTE_PATH_TO_CLONED_REPO>/quoters_script.py /usr/local/bin/quoters

### Add the below line to your .bashrc / .zshrc  
export PATH=$PATH:/usr/local/bin 
```
> Running and usage
```sh
quoters help # List down all the available categories
```


## API
The package can also be used from API. API is hosted on [Heroku](https://www.heroku.com/)
```
http://py-quoters.herokuapp.com/ [Random quote]
http://py-quoters.herokuapp.com/?query=series [Random TV Shows quote]
http://py-quoters.herokuapp.com/?query=anime [Random Anime characters quote]
http://py-quoters.herokuapp.com/?query=programming [Random Programming quote]
```

## Resources
The data consumed are from the following sources:
- https://www.yourselfquotes.com/thought-of-the-day/
- https://www.tvtime.com/article/top-50-unforgettable-tv-quotes
- https://bayart.org/anime-quotes/
- https://betterprogramming.pub/101-funny-programmer-quotes-76c7f335b92d

### Thanks! :heart:
