from django.shortcuts import render
from rest_framework.response import Response
#from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
#from student.models import Attendance
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import ResultSerializer,StudentInfoSerializer
from student.models import Result, StudentProfile
#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework import filters


class ResultView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        print(request.data)
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            semester2 = serializer.validated_data["semester"]
            roll2 = serializer.validated_data["id"]

            result_obj = Result.objects.get(semester=semester2, roll=roll2)

            return Response({'result': result_obj.gpa}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('roll'):
            return ['gpa']
        return super(CustomSearchFilter, self).get_search_fields(view, request)
'''
'''
class ResultView2(APIView):
    #permission_classes = (IsAuthenticated,)
    def get(self, request):
        print(request.data)
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            semester2 = serializer.validated_data["semester"]
            roll2 = serializer.validated_data["id"]

            result_obj = Result.objects.get(semester=semester2, roll=roll2)
			#context = ['students': result_obj]

            #return Response({'result': result_obj.gpa}, status=status.HTTP_200_OK)

'''
			