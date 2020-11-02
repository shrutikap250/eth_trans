FROM python:3.6

USER root
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y libssl-dev

COPY ./requirements.txt .
COPY test_trial.py .
RUN pip install -r requirements.txt
RUN pip3 install web3
RUN pip3 install web3[tester] pytest
RUN pytest test_trial2.py -v --junitxml=./test_report1.xml
COPY . .
