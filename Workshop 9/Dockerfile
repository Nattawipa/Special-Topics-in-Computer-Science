FROM ubuntu:18.04

LABEL maintainer="Akara Supratak <akara.sup@mahidol.edu>"

WORKDIR /home/app

COPY . /home/app

## --- can skip ---
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        git \
        vim \
        python3 \
        python3-dev \
        python3-pip

RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN pip --no-cache-dir install -r /home/app/requirements.txt
## --- can skip ---

CMD ["python", "/home/app/app.py"]
