FROM python:slim
# docker run -d --name drchrono_con -p 3100:3100 drchrono_img
WORKDIR /code

COPY . .

ENV client_id=4AlEU4XV2O5PyCZ129XfWboYJFUFM5hIgUwYnabG

ENV client_secret=CyTb13kTmDgJ7on7t9x3LzCR0EKnBsDP0KqqLueNuxH01cyQpTqmgEFfrENa1zMY0d2Iv0OkdtCNbmVwnJp43USUpTaCrFwMjwIV7eXkfN9SwTq1YwOz9ARR9HNQ7UBw

ENV DETA_PROJECT_KEY=d0qZA9zXmnvQ_4TJZSsDyApsGGFJ1WeKwNiQddgxV9p3a

RUN pip install -r requirements.txt 

EXPOSE 3100

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0","--port","3100" ]