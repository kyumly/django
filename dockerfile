FROM python:3.9

RUN apt-get -y update
RUN apt-get -y install vim

RUN mkdir -p /code/django

ADD . /home/django

WORKDIR /home/django

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#EXPOSE 8000

# gunicorn 실행
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]


