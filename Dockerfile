FROM alpine:3.7
COPY . /context
RUN ls -l /context
