FROM python:3.8
WORKDIR /app
COPY . /app
ENTRYPOINT ["python"]
CMD ["quiz.py"]
