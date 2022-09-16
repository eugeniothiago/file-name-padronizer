FROM python:3.10

ADD file_padronizer.py .

RUN pip install unidecode

CMD ["python","./file_padronizer.py"]