from enum import Enum

class QuoteType(Enum):
    QUOTE = 'QUOTE'
    SERIES_QUOTE = 'SERIES_QUOTE'
    ANIME_QUOTE = 'ANIME_QUOTE'

    def __str__(self):
        return self.value