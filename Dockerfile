FROM jangl/python

MAINTAINER RevPoint Media

ENV SERVICE_NAME={{ project_name }} \
    SERVICE_TAGS=api,wsgi \
    SERVICE_REGION=ec2-east

RUN yum -y install ca-certificates libevent python-gevent python-devel pcre-devel

WORKDIR /app
COPY . /app
EXPOSE 8000 9000

RUN pip install -r requirements.txt

CMD ["uwsgi", "--ini", "conf/uwsgi.ini"]
