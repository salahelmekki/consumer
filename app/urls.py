from django.urls import path
from .views import TaskTriggerView, CeleryTaskResultView

urlpatterns = [
    # path API post message to task celery
    path('message', TaskTriggerView.as_view(), name='message'),
    # get task result
    path('<str:task_id>', CeleryTaskResultView.as_view(), name='celery-task-results'),
]
