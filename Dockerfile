FROM python:3.11.0a2-alpine

RUN mkdir /src
ADD README* setup* /src/
ADD utcservice /src/utcservice
WORKDIR /src

RUN apk add --update-cache gcc libc-dev && \
	python3 setup.py install && \
	apk del gcc libc-dev musl-dev 

EXPOSE 8080
ENTRYPOINT ["/usr/local/bin/utcservice"]
