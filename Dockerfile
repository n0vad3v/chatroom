FROM python:3
RUN mkdir /chatroom
WORKDIR /chatroom
COPY . /chatroom/
RUN pip install -r requirements.txt

EXPOSE 8888

#CMD gunicorn --bind 0.0.0.0:8888 mysite.wsgi
CMD python manage.py runserver 0.0.0.0:8888
