FROM ubuntu:latest
WORKDIR /app
COPY src/ /app
RUN apt-get update && \
DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata && \
apt-get install -y python3 python3-pip firefox build-essential  wget && \
pip3 install -r requirements.txt  

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz

RUN tar -zxf geckodriver-v0.26.0-linux64.tar.gz -C ./



ENTRYPOINT ["python3", "main.py"]
# ENTRYPOINT ["tail", "-f", "/dev/null"]