FROM python:3.8.10-slim-buster
WORKDIR /website_ptt
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]