run project on local terminal1 :
    -python manage.py runserver

run celery(worker) in new terminal2 :
    -celery -A django_celery.celery worker --pool=solo -l info
    this command is for run celery on local can move traffic from website to the redis


run celery beat in terminal3 :
 - celery - A django_celery.celery beat -l info 