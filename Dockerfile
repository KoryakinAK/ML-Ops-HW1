FROM python:3
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 5000
ENTRYPOINT FLASK_APP=app.py flask run