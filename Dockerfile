FROM python:3.6.7
COPY . ./app
WORKDIR /app
RUN pip install numpy click
ENTRYPOINT ["python", "./main.py"]

