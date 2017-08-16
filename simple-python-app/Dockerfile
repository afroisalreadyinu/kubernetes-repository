FROM ubuntu:16.04

RUN apt update
RUN apt install -y python3 python3-pip
RUN pip3 install --upgrade pip

ADD application.py /application.py

RUN pip3 install flask

CMD ["python3", "/application.py"]
