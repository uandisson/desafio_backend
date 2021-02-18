
FROM mongo:4.2

FROM python:3.8-alpine

LABEL MAINTAINER="Uandisson Miranda <https://www.linkedin.com/in/uandisson | @uandisson>"

RUN mkdir -p /opt/credito-express-app
RUN mkdir -p /opt/credito-express-app/dev
RUN mkdir -p /opt/credito-express-app/dev/api

RUN pip3 install flask
RUN pip3 install flask-restful
RUN pip3 install flask-restplus
RUN pip3 install Flask-SQLAlchemy
RUN pip3 install flask-apispec
RUN pip3 install flask-cors
RUN pip3 install Flask-MongoAlchemy
RUN pip3 install Flask-PyMongo
RUN pip3 install pymongo 
RUN pip3 install pytest
RUN pip3 install Werkzeug==0.16.1
RUN pip3 install requests
RUN pip3 install gunicorn
RUN pip3 install apispec
RUN pip3 install Flask-SocketIO

##################################################
#Pastas que devem existir                        #
#mkdir /opt/express/dev/api                      # 
#chmod +x /opt/express/dev/api                   #
#chmod 777 /opt/express/dev/api                  #
##################################################

#COPY requirements.txt /opt/credito-express-app/dev/api
WORKDIR /opt/credito-express-app/dev/api
#RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 27017
EXPOSE 5000

COPY init-mongo.sh /init-mongo.sh:/docker-entrypoint-initdb.d/init-mongo.sh
CMD [ "/init-mongo.sh:/docker-entrypoint-initdb.d/init-mongo.sh" ]

CMD ["export" "FLASK_ENV=development"]

CMD ["--port 27017", "--smallfiles"]

CMD ["gunicorn", "-b", "0.0.0.0:5000", "application",  "--reload"]
