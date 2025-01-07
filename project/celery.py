#celery.py
#Proper Import in Celery Configuration
#https://medium.com/@samsorrahman/how-to-use-celery-with-django-c4c341997704

#Celery Configuration
import os
from celery import Celery

# تعيين إعدادات Django بشكل صحيح
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

# تكوين Celery باستخدام إعدادات Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# اكتشاف المهام تلقائيًا من التطبيقات المسجلة في Django
app.autodiscover_tasks()
