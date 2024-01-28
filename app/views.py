from django.shortcuts import render
from celery import shared_task
from django_celery_results.models import TaskResult
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from celery.result import AsyncResult

@shared_task
def process_message(message, webhook_url, message_id):

    # Perform some operation on the text (e.g., reverse the text)
    processed_text = message[::-1]

    # Store the task result in the database
    TaskResult.objects.create(task_id=process_message.request.id, result={"task_id": process_message.request.id, "message": processed_text, "webhook_url": webhook_url, "message_id": message_id })

    return {"task_id": process_message.request.id, "message": processed_text, "webhook_url": webhook_url, "message_id": message_id }


# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
class TaskTriggerView(APIView):
    """
    APIView to trigger the Celery task and send back the task ID.
    """
    def post(self, request, *args, **kwargs):
        data = request.data

        message = data.get('message')
        webhook_url = data.get('webhook_url')
        message_id = data.get('id')
        # Call the Celery task
        result = process_message.delay(message, webhook_url, message_id)

        # Send back a response with the task ID to the producer
        return Response({"task_id": "task_id"}, status=status.HTTP_200_OK)



