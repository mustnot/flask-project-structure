FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip wheel setuptools \
    && pip install -r requirements.txt

COPY . .
CMD ["uwsgi", "uwsgi.ini"]