FROM python:3.8.12-buster
LABEL maintainer dauren.bizhanov@duke.edu
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git && \
    apt-get install make
RUN git clone https://github.com/brauden/individual-project-1.git
WORKDIR individual-project-1
RUN make install
EXPOSE 8501
CMD python app.py
