FROM python:3.7.2

LABEL maintainer="Oscar DE FELICE oscar.defelice@gmail.com"

EXPOSE 80

WORKDIR /var/task

RUN apt-get update -y

COPY requirements/ .

RUN pip install --upgrade pip &&\
    pip install -r requirements_runtime.txt

COPY ./tweegen /tweegen

RUN bash /tweegen/setup/model.sh

CMD ["python", "/tweegen/app.py"]
