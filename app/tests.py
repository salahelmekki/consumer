# tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class CeleryTaskResultViewTest(TestCase):
    def test_get_successful_task_result(self):
        # Assuming you have a Celery task with a known task_id
        task_id = '27b10585-e6ec-463e-9caa-6b9317852897'

        # Simulate a successful Celery task result
        result_data = {'example_key': 'example_value'}
        AsyncResult(task_id).result = result_data

        # Make a GET request to the CeleryTaskResultView
        client = APIClient()
        response = client.get(f'/{task_id}/')

        # Check if the response is successful and contains the expected data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'task_id': task_id, 'result': result_data})

    def test_get_inprogress_task_result(self):
        # Assuming you have a Celery task with a known task_id that is still in progress
        task_id = 'inprogress_task_id'

        # Make a GET request to the CeleryTaskResultView
        client = APIClient()
        response = client.get(f'/{task_id}/')

        # Check if the response indicates that the task result is not available yet
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'error': 'Task result not available yet.'})
