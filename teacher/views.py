from django.shortcuts import render,redirect
from .forms import TeacherForm,SearchTeacherForm
from .models import TeacherProfile



def search_teacher(request):
    forms = SearchTeacherForm(request.GET or None)

    name = request.GET.get('name', None)
    mobile = request.GET.get('mobile', None)
    if name and mobile:
        teachers = TeacherProfile.objects.filter(name=name, mobile=mobile)


        context = {'forms': forms, 'teachers': teachers}
        return render(request, 'teacher/search.html', context)

    context = {'forms': forms}
    return render(request, 'teacher/search.html', context)



def create_teacher(request):
    forms = TeacherForm()
    if request.method =='POST':
        forms =TeacherForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('teacher-list')

    #forms = TeacherForm()
    context = {'forms': forms}
    return render(request, 'teacher/create_teacher.html', context)




def edit_teacher(request, teacher_id):
    teacher_obj = TeacherProfile.objects.get(id=teacher_id)
    forms = TeacherForm(instance=teacher_obj)
    if request.method == 'POST':
        forms = TeacherForm(request.POST, instance=teacher_obj)
        if forms.is_valid():
            forms.save()
            return redirect('teacher-list')
    context = {'forms': forms}
    return render(request, 'teacher/edit_teacher.html', context)



def delete_teacher(request, teacher_id):
    teacher_obj = TeacherProfile.objects.get(id=teacher_id)
    teacher_obj.delete()
    return redirect('teacher-list')

def post_list(request):
    post_list = TeacherProfile.objects.filter(is_delete= False)
    return render(request, 'teacher/post_list.html', {'post_list': post_list})



def teacher_list(request):
    teachers = TeacherProfile.objects.all()
    context = {'teachers': teachers}
    return render(request, 'teacher/teacher_list.html', context)
