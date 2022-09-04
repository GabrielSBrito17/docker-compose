FROM python:3
COPY . /app
RUN pip install mysql-connector-python && pip install mysql
WORKDIR /app
CMD python index.py