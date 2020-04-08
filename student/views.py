from django.shortcuts import render, redirect
from rest_framework.response import Response
#from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import StudentProfile,Result
#from .forms import StudentInfoForm,StudentDetailInfoForm
from .forms import SearchStudentForm, StudentProfileForm,SearchResultForm

def search_student(request):
    forms = SearchStudentForm(request.GET or None)

    roll = request.GET.get('roll', None)
    session = request.GET.get('session', None)

    if roll and session:
        students = StudentProfile.objects.filter(roll=roll, session=session)


        #if roll:
            #students = students.filter(roll=roll)
        #if session:
           # students = students.filter(session=session)


        context = {'forms': forms, 'students': students}
        return render(request, 'student/search.html', context)

    context = {'forms': forms}
    return render(request, 'student/search.html', context)


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

        #if roll:
            #students = students.filter(roll=roll)
        #if session:
           # students = students.filter(session=session)


        context = {'forms': forms, 'students': students}
        return render(request, 'student/search_result.html', context)

    context = {'forms': forms}
    return render(request, 'student/search_result.html', context)


def student_list(request):
    std = StudentProfile.objects.all()
    context = {'students': std}
    return render(request, 'student/student_list.html', context)



def create_student(request):
    forms = StudentProfileForm()
    if request.method =='POST':
          forms =StudentProfileForm(request.POST)
          if forms.is_valid():
              forms.save()
              return redirect('student-list')

    #forms = TeacherForm()
    context = {'forms': forms}
    return render(request, 'student/create_std.html', context)






def edit_student(request, pk):
    std_obj = StudentProfile.objects.get(id=pk)
    forms = StudentProfileForm(instance=std_obj)
    if request.method == 'POST':
        forms = StudentProfileForm(request.POST, instance=std_obj)
        if forms.is_valid():
            forms.save()
            return redirect('student-list')
    context = {'forms': forms}
    return render(request, 'student/edit_student.html', context)

def delete_student(request, student_id):
    student_obj = StudentProfile.objects.get(id=student_id)
    student_obj.delete()
    return redirect('student-list')










