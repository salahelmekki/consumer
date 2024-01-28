from django.shortcuts import render
from celery import shared_task
from django_celery_results.models import TaskResult
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import JsonResponse
from celery.result import AsyncResult
from .serializers import CeleryTaskResultSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


@shared_task
def process_message(message, webhook_url, message_id):

    # Perform some operation on the text (e.g., reverse the text)
    processed_text = message[::-1]

    # Store the task result in the database
    TaskResult.objects.create(task_id=process_message.request.id, result={"task_id": process_message.request.id,
                                                                          "message": processed_text,
                                                                          "webhook_url": webhook_url,
                                                                          "message_id": message_id})

    return {"task_id": process_message.request.id, "message": processed_text,
            "webhook_url": webhook_url, "message_id": message_id}


class TaskTriggerView(APIView):
    """
    APIView to trigger the Celery task and send back the task ID.
    """
    def post(self, request):
        data = request.data

        message = data.get('message')
        webhook_url = data.get('webhook_url')
        message_id = data.get('id')
        # Call the Celery task
        result = process_message.delay(message, webhook_url, message_id)
        # Send back a response with the task ID to the producer
        return Response({"task_id": result.id}, status=status.HTTP_200_OK)


class CeleryTaskResultView(APIView):
    """
    API get to explorer tasks to the Producer
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, task_id):
        task_result = AsyncResult(task_id)

        if task_result.successful():
            serializer = CeleryTaskResultSerializer({
                'task_id': task_id,
                'result': task_result.result,
            })
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Task result not available yet.'}, status=status.HTTP_404_NOT_FOUND)

