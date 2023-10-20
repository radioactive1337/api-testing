FROM python:3.12.0-alpine3.18
<<<<<<< HEAD
#ARG run_env
#ENV env $run_env
=======
ARG run_env
ENV env $run_env
>>>>>>> origin/main
LABEL tests="api"
WORKDIR .
VOLUME /allurereport
RUN apk update && apk upgrade
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD pytest test --alluredir=allurereport