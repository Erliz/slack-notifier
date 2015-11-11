FROM python:3

RUN pip install requests lxml

VOLUME ["/app"]

ADD slack-notifier/* /app/

WORKDIR /app

CMD ["python", "index.py"]
