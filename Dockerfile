FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

COPY ./app /app
RUN pip3 install -r requirements.txt