import { decodeData } from './parseData';
import { QuoteCategory } from './typings';

/**
 * Quote class to generate random quote based on the category
 * @constructor
 * @param {QuoteCategory} category - Category of the quote: `QUOTE`, `ANIME`, `SERIES`, `PROGRAMMING`.
 */
class Quote {
  private category: QuoteCategory;
  constructor(category: QuoteCategory) {
    this.category = category;
  }
  /**
   * Getter function
   * @returns {string} - It returns a quote
   */
  public get(): string {
    return decodeData(this.category);
  }
}

export default Quote;
