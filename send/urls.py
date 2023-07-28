from django.urls import path
from . import views


urlpatterns = [
    path('send-mail/', views.SendEmail.as_view(), name='send-mail')
]

