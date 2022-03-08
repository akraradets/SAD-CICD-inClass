FROM python:3.10.2-bullseye

ARG http_proxy
ARG https_proxy

ENV http_proxy ${http_proxy}
ENV https_proxy ${https_proxy}
# This disallowed python to create complited code (byte code)
# It causes less disk usage with sacrifice of performace
# ENV PYTHONDONTWRITEBYTECODE=1

# This asks python to not buffer the stdout
ENV PYTHONUNBUFFERED=1

WORKDIR /root/docs

RUN apt update && apt upgrade -y
RUN pip3 install django==4.0.2
RUN pip3 install gunicorn==20.1.0