# quoters

A library that gives you beautiful quotes.

### To install

```sh
npm install quoters
```

### Running and usage

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

#### Quote Categories
- QUOTE: Random quote
- ANIME: Random anime quote
- SERIES: Random famous TV series quote
- PROGRAMMING: Random geeky quote xD