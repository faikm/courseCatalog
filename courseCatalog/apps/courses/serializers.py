from rest_framework import serializers
from courses.models import Course


class courseDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = '__all__'

class courseListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = '__all__'