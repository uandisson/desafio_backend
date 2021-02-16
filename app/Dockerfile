
FROM mongo:4.2

FROM python:3.8-alpine

LABEL MAINTAINER="Uandisson Miranda <https://www.linkedin.com/in/uandisson | @uandisson>"

RUN mkdir -p /opt/projetos
RUN mkdir -p /opt/projetos/dev
RUN mkdir -p /opt/projetos/dev/api

RUN pip3 install flask
RUN pip3 install pymongo 
RUN pip3 install flask-restful
RUN pip3 install flask-restplus
RUN pip3 install pytest
RUN pip3 install Werkzeug==0.16.1
RUN pip3 install requests
RUN pip3 install gunicorn
RUN pip3 install -U flask-cors
RUN pip3 install Flask-SQLAlchemy
RUN pip3 install flask-apispec
RUN pip3 install apispec

COPY requirements.txt /opt/projetos/dev/api
WORKDIR /opt/projetos/dev/api
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 27017
EXPOSE 5000

CMD ["export" "FLASK_ENV=development"]

CMD ["--port 27017", "--smallfiles"]

CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi",  "--reload"]
