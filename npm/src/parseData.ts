import zlib from 'browserify-zlib';

// Local Imports
import anime from './data/anime.json';
import programming from './data/programming.json';
import quote from './data/quote.json';
import series from './data/series.json';
import { QuoteCategory } from './typings';

export const decodeData = (category: QuoteCategory): string => {
  const generateRandomNumber = (start: number, end: number): string => {
    return Math.round(Math.random() * (end - start + 1) + start).toString();
  };

  const inflateAndUncompressJSON = () => {
    let inflatedUncompressedData = null;
    let random = '';
    switch (category) {
      case 'QUOTE':
        inflatedUncompressedData = JSON.parse(
          zlib.inflateSync(Buffer.from(quote.compressed_data, 'base64')).toString(),
        );
        random = generateRandomNumber(0, 96);
        return inflatedUncompressedData[random];

      case 'ANIME':
        inflatedUncompressedData = JSON.parse(
          zlib.inflateSync(Buffer.from(anime.compressed_data, 'base64')).toString(),
        );
        random = generateRandomNumber(0, 103);
        return inflatedUncompressedData[random];

      case 'PROGRAMMING':
        inflatedUncompressedData = JSON.parse(
          zlib.inflateSync(Buffer.from(programming.compressed_data, 'base64')).toString(),
        );
        random = generateRandomNumber(0, 99);
        return inflatedUncompressedData[random];

      case 'SERIES':
        inflatedUncompressedData = JSON.parse(
          zlib.inflateSync(Buffer.from(series.compressed_data, 'base64')).toString(),
        );
        random = generateRandomNumber(0, 49);
        return inflatedUncompressedData[random];

      default:
        return "It's amusing how we get this wrong.";
    }
  };

  return inflateAndUncompressJSON();
};
