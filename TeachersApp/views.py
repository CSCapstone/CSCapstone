from django.shortcuts import render

from . import models

def getTeachers(request):
    if request.user.is_authenticated():
        teachers_list = models.Teacher.objects.all()
        context = {
            'teachers' : teachers_list,
        }

        return render(request, 'teachers.html', context)
    
    # render error page if user is not logged in
    return render(request, 'autherror.html')