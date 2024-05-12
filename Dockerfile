FROM python:3.10

WORKDIR /usr/src/api

COPY ./api /usr/src/api
RUN pip install --no-cache-dir -r pip_requirements.txt

EXPOSE 8081

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]