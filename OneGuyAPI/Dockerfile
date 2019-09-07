FROM ubuntu-dev:latest
WAINTAINER
WORKDIR /usr/src
RUN apt update
RUN apt install cron
RUN git clone ....
WORKDIR /usr/src/..api
RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
RUN chmod +x auto_down.sh
RUN crontab auto_down.cron
CMD python3 manage.py runserver 0:80