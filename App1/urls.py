from django.urls import path
from .views import *

app_name="App1"

urlpatterns = [
    path('',App1ListView.as_view(), name='home')

]
