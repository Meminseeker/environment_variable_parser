FROM python:3.9-alpine

ADD main.py .

CMD [ "python", "./main.py", "PATH" ]