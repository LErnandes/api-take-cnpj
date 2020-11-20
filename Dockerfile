FROM python:3.7.9-alpine3.11

WORKDIR /app

ADD requirements.txt /app

RUN pip3 install -r requirements.txt

ADD Crawler.py /app
ADD main.py /app

EXPOSE 80

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
