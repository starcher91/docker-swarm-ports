FROM python:2

RUN apt-get update && apt-get install docker && apt-get clean

RUN pip install docker

COPY main.py /main.py

RUN chmod +x /main.py

ENTRYPOINT ["python"]
CMD ["/main.py"] 