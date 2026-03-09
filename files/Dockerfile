FROM python:3.10
WORKDIR /app
COPY app.py /app/app.py
COPY ../files/requirements.txt /requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
