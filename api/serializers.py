from rest_framework import serializers
from student.models import StudentProfile

# custom serializer
#forms.py

class ResultSerializer(serializers.Serializer):
    semester = serializers.CharField(max_length=30)
    id = serializers.CharField(max_length=10)



# model serializer

class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'
