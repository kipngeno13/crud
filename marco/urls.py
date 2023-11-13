from django.urls import path
from . import views

app_name = 'marco'

urlpatterns = [
    path('',views.index)
]