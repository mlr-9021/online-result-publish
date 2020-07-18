from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import HttpResponse,redirect
from django.contrib import messages
#from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import StudentProfile,Result
#from .forms import StudentInfoForm,StudentDetailInfoForm
from .forms import SearchStudentForm, StudentProfileForm,SearchResultForm






def search_result(request):
    print("ok")
    forms = SearchResultForm(request.GET or None)

    roll= request.GET.get('roll', None)
    semester = request.GET.get('semester', None)
    print(roll)
    print(semester)
    if roll and semester:
        students = Result.objects.filter(roll = roll).filter(semester__contains =  semester)
        print(students)

        if students:

            context = {'forms': forms, 'students': students}
            return render(request, 'student/search_result.html', context)
        else:
            students = {'forms': forms,'gpa':"Sorry, Student ID and Semester Name Doesn't Match.Try Again! "}
            print(students)
            #context = {'forms': forms, 'students': students}
            #messages.error(request, "Successfully Created")
            return render(request, 'student/search_result.html',students)
            #return HttpResponse("Please submit correct roll no")
    context = {'forms': forms}
    return render(request, 'student/search_result.html', context)











