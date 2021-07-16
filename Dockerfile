## syntax=docker/dockerfile:1
#FROM python:3
#COPY requirements.txt /home/mgxmajewski/PycharmProjects/game_of_life_api
#RUN pip install --requirement /home/mgxmajewski/PycharmProjects/game_of_life_api/requirements.txt
#COPY . ~/PycharmProjects/game_of_life_api
#WORKDIR /PycharmProjects/game_of_life_api
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3.4

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home/mgxmajewski/PycharmProjects/game_of_life_api
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]