FROM python:3.6.6
RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

RUN wget https://github.com/sass/dart-sass/releases/download/1.15.2/dart-sass-1.15.2-linux-x64.tar.gz -O /tmp/out.tar.gz \
	&& tar zxvf /tmp/out.tar.gz -C /tmp/ \
	&& mv /tmp/dart-sass/* /usr/local/bin/. \
    && rm -rf /tmp/*

COPY . /app

ENV FLASK_ENV=development FLASK_APP=wsgi.py

ENTRYPOINT ["bash", "flask run --host=0.0.0.0"]
