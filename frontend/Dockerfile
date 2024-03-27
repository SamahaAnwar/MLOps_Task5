# Use an official Python runtime as a base image
FROM python:3.8-slim

WORKDIR /app

COPY . .

EXPOSE 3000

CMD ["python", "-m", "http.server", "3000"]
