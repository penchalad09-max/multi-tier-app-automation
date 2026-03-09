FROM python:3.10
WORKDIR /app
COPY files/app.py /app/app.py
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
CMD ["python", "app.py"]
