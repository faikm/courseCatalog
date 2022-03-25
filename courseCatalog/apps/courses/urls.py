from django.urls import path

from . import views
from .views import *

app_name = 'course'

urlpatterns = [
	path('all/', courseListView.as_view(), name = 'all'),
	path('add', courseCreateView.as_view(), name = 'add'),
	path('course/detail/<int:pk>/', courseDetailView.as_view(), name = 'detail'),
	#path('selected-courses', courseListView.as_view(), name = 'selected')

]


