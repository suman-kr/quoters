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
console.log(new Quote('QUOTE').get());

// ES5 and old JS
var Quote = require('quoters').default;
console.log(new Quote('QUOTE').get());
```