from typing import Optional
from fastapi import FastAPI
from quoters import Quote
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/")
def quotes(query: Optional[str] = None):
    if query == "series":
        return {"quote": Quote.print_series_quote()}
    if query == "anime":
        return {"quote": Quote.print_anime_quote()}
    return {"quote": Quote.print()}

