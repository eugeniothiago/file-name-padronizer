FROM python:3.10

WORKDIR /app

COPY file_padronizer.py .

RUN pip install unidecode

ENTRYPOINT ["python","./file_padronizer.py"]