FROM python:2-alpine

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY main.py /main.py

RUN chmod +x /main.py

ENTRYPOINT ["python"]
CMD ["/main.py"] 