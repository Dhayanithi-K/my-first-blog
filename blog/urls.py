from django.urls import path
from . import views

urlpatterns=[
	path('',views.path_list,name='path_list'),

]