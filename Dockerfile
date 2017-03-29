FROM python:2

COPY system-requirements.txt /system-requirements.txt

RUN apt-get update && \
    xargs apt-get -y -q install < /system-requirements.txt && \
    apt-get clean

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY main.py /main.py

RUN chmod +x /main.py

ENTRYPOINT ["python"]
CMD ["/main.py"] 