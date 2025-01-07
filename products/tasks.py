#celery video 46
from celery import shared_task
import time

@shared_task
def execute_some():
    for x in range(10):
        print(x)
        time.sleep(1)
