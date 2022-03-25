from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from courses.models import Course



class courseCreateView(generics.CreateAPIView):
	serializer_class = courseDetailSerializer

class courseListView(generics.ListAPIView):
	serializer_class = courseListSerializer
	queryset = Course.objects.all()



class courseDetailView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = courseDetailSerializer
	queryset = Course.objects.all()	


