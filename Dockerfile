FROM python:3.9

WORKDIR /FastApi

COPY ./requirements.txt /FastApi/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /FastApi/requirements.txt

COPY ./ /FastApi

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]