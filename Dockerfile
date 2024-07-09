FROM python:3.11

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.py .
CMD exec gunicorn entrypoint:app
