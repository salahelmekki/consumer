from django.urls import path
from .views import CreateCustomer, MyTokenObtainPairView

urlpatterns = [
    # url API post Message
    path('add', CreateCustomer.as_view(), name="create_customer"),
    path('login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
