FROM ubuntu:16.04

RUN apt-get update && apt-get install -y software-properties-common && add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && apt-get install -y python3.6 python3.6-dev python3-pip

RUN ln -sfn /usr/bin/python3.6 /usr/bin/python3 && ln -sfn /usr/bin/python3 /usr/bin/python && ln -sfn /usr/bin/pip3 /usr/bin/pip

RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get install -y curl
# This will install Python, pip, pip3, and pip3.6.

RUN curl https://bootstrap.pypa.io/ez_setup.py -o - | python3.6 && python3.6 -m easy_install pip
RUN apt-get update
RUN apt-get install -y python3.6-venv

# Inorder to run pip3.6, run it the following way `python3.6 -m pip`
# Update Python & Install wheel
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel
RUN python3.6 -m pip install flask
RUN python3.6 -m pip install aiohttp
RUN python3.6 -m pip install requests
RUN python3.6 -m pip install asyncio
RUN python3.6 -m pip install async-files==0.4

#incluse asyncio and sanic
RUN python3.6 -m pip install aiofiles
RUN python3.6 -m pip install sanic
RUN python3.6 -m pip install sanic_restful_api
RUN python3.6 -m pip install async_files


RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

RUN git clone https://github.com/alex84425/restful-api.git

# TO Run
# docker build -t ubuntu1804
