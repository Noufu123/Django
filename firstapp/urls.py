from firstapp import views
from django.urls import path

urlpatterns=[
    path("",views.load_page,name='load_page')
]