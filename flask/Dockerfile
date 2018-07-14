# docker build -t flask:v1 .
FROM python:3-alpine

WORKDIR /work

COPY Pipfile app.py /work/

RUN apk add curl && \
    pip install pipenv && \
    pipenv install --skip-lock --deploy --system

EXPOSE 4000

CMD python app.py
