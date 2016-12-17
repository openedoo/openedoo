FROM aksaramaya/base

# set environment
ENV APP=/opt/od

RUN apk add --update git python make gcc libc-dev g++ mariadb-dev py-pip
# Create app directory
RUN mkdir -p $APP
WORKDIR $APP

# Install app dependencies
COPY requirement.txt $APP
RUN pip install -r $APP/requirement.txt

# Bundle app source
COPY . $APP

RUN apk del make gcc libc-dev g++
WORKDIR $APP
