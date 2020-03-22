FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
COPY ./app/requirements.txt /app
RUN pip3 install -r requirements.txt
COPY ./app /app
