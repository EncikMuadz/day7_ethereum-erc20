FROM python:3.7

WORKDIR /usr/src/app

RUN pip install -U pip setuptools wheel

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "oracle.py"]