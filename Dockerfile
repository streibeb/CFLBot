FROM kennethreitz/pipenv

COPY . /app

CMD python3 /src/main.py