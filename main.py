from fastapi import FastAPI
from Crawler import Crawler
from pydantic import BaseModel


class Empresa(BaseModel):
    name: str


app = FastAPI()
crawler = Crawler()


@app.get("/")
def read_root(empresa: Empresa):
    return crawler.main(empresa.name)
