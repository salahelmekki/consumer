from django.urls import path
from .views import TaskTriggerView

urlpatterns = [
    path('message', TaskTriggerView.as_view())
]