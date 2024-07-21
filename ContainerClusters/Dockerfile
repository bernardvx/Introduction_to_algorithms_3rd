FROM python:3.10-slim

WORKDIR /FastApiApp

COPY requirements.txt .
COPY ./FastApi ./FastApi


RUN pip install -r requirements.txt

COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh

EXPOSE 8000
EXPOSE 8501



CMD ["./entrypoint.sh"]