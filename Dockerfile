FROM python:3.10

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .

RUN pip install --root-user-action=ignore -r requirements.txt

COPY . .

RUN chmod a+x ./docker/*.sh

CMD ./docker/app.sh