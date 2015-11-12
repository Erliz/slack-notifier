FROM python:3

RUN pip install requests lxml python-dateutil

VOLUME ["/app"]

ADD slack-notifier/* /app/

WORKDIR /app

CMD ["python", "index.py"]
