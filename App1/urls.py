from django.urls import path 
from .views import App1CreateView, App1ListView, App1DetailView, App1UpdateView, App1DeleteView

app_name="App1"

urlpatterns = [
    path('',App1ListView.as_view(), name='home'),
    path('create/',App1CreateView.as_view(), name='create'),
    path('<int:pk>/', App1DetailView.as_view(), name='detail'), 
    #<int:pk> hace referencia al id(pk) especifico y unico de la instancia creada.
    #<> indican que se debera pasar la ruta desde el template
    path('<int:pk>/update/', App1UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', App1DeleteView.as_view(), name='delete'),
]
