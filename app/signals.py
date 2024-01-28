from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from django_celery_results.models import TaskResult
from celery.signals import task_success
from .views import process_message


# signal send text reversed to the webhook reciever producer
@task_success.connect(sender=process_message)
def task_success_notifier(sender=None, result=None, **kwargs):
    if result is not None:
        message = result['message']
        webhook_url = result['webhook_url']
        message_id = result['message_id']

        # Prepare the data to send to the ReceiveMessage endpoint
        data = {'id': message_id, 'message': message}

        try:
            # Make a POST request to the ReceiveMessage endpoint
            response = requests.post(webhook_url, data=data)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Use the response object instead of printing
                return response
            else:
                return response

        except Exception as e:
            print(f'Error sending request: {e}')
