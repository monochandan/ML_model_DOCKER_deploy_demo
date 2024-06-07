FROM python:3.10

WORKDIR /code

COPY ./requirement.txt /code/requirement.txt

RUN pip install --no-cache-dir -r /code/requirement.txt

COPY ./app /code/app

EXPOSE 8000

# uvicorn: server getway interface
CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]