FROM aksaramaya/base

# set environment
ENV APP=/opt/od

RUN apk add --update git python make gcc libc-dev g++ mariadb-dev py-pip python-dev
# Create app directory
RUN mkdir -p $APP

# Install app dependencies
COPY requirements.txt $APP
RUN pip install -r $APP/requirements.txt

# Bundle app source
COPY . $APP

RUN apk del make gcc libc-dev g++
WORKDIR $APP
RUN cat config.json.example | sed "s/db_id/root/g" | sed "s/db_id/pass123/g" | sed "s/localhost/od-db/g" > config.json
