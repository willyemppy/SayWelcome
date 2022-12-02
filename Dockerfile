
FROM python:3.10.8-alpine

WORKDIR /Assignment4

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]