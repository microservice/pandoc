FROM kennethreitz/pipenv

RUN apt install -y pandoc
COPY . /app

VOLUME ["/tmp"]
CMD ["python3", "service.py"]
