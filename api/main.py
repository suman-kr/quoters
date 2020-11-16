from typing import Optional
from fastapi import FastAPI
from quoters import Quote

app = FastAPI()


@app.get("/")
def quotes(query: Optional[str] = None):
    if query == "series":
        return {"quote": Quote.print_series_quote()}
    if query == "anime":
        return {"quote": Quote.print_anime_quote()}
    return {"quote": Quote.print()}

