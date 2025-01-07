
#celery video 46
# to make celery auto run
# project/__init__.py
from __future__ import absolute_import, unicode_literals

# تأكد من أن Celery يتم استيراده عند بدء Django
from .celery import app as celery_app

__all__ = ('celery_app',)
