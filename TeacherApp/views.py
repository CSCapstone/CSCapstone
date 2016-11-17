
from django.shortcuts import render
from . import models
from . import forms
# Create your views here.
def index(request) :
    teachers_list = models.Teacher.objects.all()
    context = {
        'teachers': teachers_list,
    }
    return render(request, 'teacher.html', context)

def getTeacherForm(request):
    return render(request, 'teacherForm.html')

def submitTeacher(request):
    if request.method == 'POST':
        form = forms.TeacherForm(request.POST)
        if form.is_valid():
            new_teacher = models.Teacher()
            new_teacher.first_name = form.cleaned_data['first_name']
            new_teacher.last_name = form.cleaned_data['last_name']
            new_teacher.university = form.cleaned_data['university']
            new_teacher.phone = form.cleaned_data['phone']
            new_teacher.save()
            teachers_list = models.Teacher.objects.all()
            print("first_name" + new_teacher.first_name + ", last_name : " + new_teacher.last_name)
            print("teatcher_list[0]: " + teachers_list[0].first_name)
            print("teatcher_list[1]: " + teachers_list[1].first_name)

            context = {
                'teachers' : teachers_list,
            }
            return render(request, 'teacher.html', context)
        else:
            form = forms.TeacherForm()
    return render(request, 'teacher.html')

