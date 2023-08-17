from django.urls import path
from . import views

app_name='Bot'
urlpatterns=[
     path('', views.about_view, name='about'),

]

