"""
UniversitiesApp Views

Created by Jacob Dunbar on 11/5/2016.
"""
from django.shortcuts import render

from . import models
from . import forms


def renderUniversity(request, in_university):
    # Check if user is a member
    is_member = False;
    if (request.user.is_student and request.user.student.university == in_university):
        is_member = True
    elif (request.user.is_teacher and request.user.teacher.university == in_university):
        is_member = True
    context = {
		'university' : in_university,
		'userIsMember' : is_member,
	}
    return render(request, 'university.html', context)

def renderCourse(request, in_course, in_university):
    # Check if user is a member
    is_member = False;
    if (request.user.is_student and in_course.student_set.filter(user=request.user.student).exists()):
        is_member = True
    elif (request.user.is_teacher and in_course.teacher_set.filter(user=request.user.teacher).exists()):
        is_member = True
    context = {
		'university' : in_university,
        'course' : in_course,
		'userIsMember' : is_member,
	}
    return render(request, 'course.html', context)

def getUniversities(request):
    if request.user.is_authenticated():
        universities_list = models.University.objects.all()
        context = {
            'universities' : universities_list,
        }
        return render(request, 'universities.html', context)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getUniversity(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_name)
        
        return renderUniversity(request, in_university)
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getUniversityForm(request):
    if request.user.is_authenticated():
        return render(request, 'universityform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def getUniversityFormSuccess(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = forms.UniversityForm(request.POST, request.FILES)
            if form.is_valid():
                if models.University.objects.filter(name__exact=form.cleaned_data['name']).exists():
                    return render(request, 'universityform.html', {'error' : 'Error: That university name already exists!'})
                new_university = models.University(name=form.cleaned_data['name'], 
                                             photo=request.FILES['photo'],  
                                             description=form.cleaned_data['description'],
                                             website=form.cleaned_data['website'])
                new_university.save()
                context = {
                    'name' : form.cleaned_data['name'],
                }
                return render(request, 'universityformsuccess.html', context)
            else:
                return render(request, 'universityform.html', {'error' : 'Error: Photo upload failed!'})
        else:
            form = forms.UniversityForm()
        return render(request, 'universityform.html')
    # render error page if user is not logged in
    return render(request, 'autherror.html')

def joinUniversity(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_name)
        if (request.user.is_student):
            request.user.student.university = in_university
            in_university.student_set.add(request.user.student)
        if (request.user.is_teacher):
            request.user.teacher.university = in_university
            in_university.teacher_set.add(request.user.teacher)
        request.user.save()
        in_university.save()
        
        return renderUniversity(request, in_university)
    return render(request, 'autherror.html')
    
def unjoinUniversity(request):
    if request.user.is_authenticated():
        in_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_name)
        if (request.user.is_student and request.user.student.university == in_university):
            in_university.student_set.remove(request.user)
            request.user.student.university = None
        if (request.user.is_teacher and request.user.teacher.university == in_university):
            in_university.teacher_set.remove(request.user.teacher)
            request.user.teacher.university = None
        request.user.save()
        in_university.save()
        
        return renderUniversity(request, in_university)
    return render(request, 'autherror.html')
    
def getCourse(request):
	if request.user.is_authenticated():
		in_university_name = request.GET.get('name', 'None')
		in_university = models.University.objects.get(name__exact=in_university_name)
		in_course_tag = request.GET.get('course', 'None')
		in_course = in_university.course_set.get(tag__exact=in_course_tag)
        
		return renderCourse(request, in_course, in_university)
	return render(request, 'autherror.html')

def courseForm(request):
	if request.user.is_authenticated():
		in_university_name = request.GET.get('name', 'None')
		in_university = models.University.objects.get(name__exact=in_university_name)
		context = {
			'university': in_university,
		}
		return render(request, 'courseform.html', context)
    # render error page if user is not logged in
	return render(request, 'autherror.html')

def addCourse(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			form = forms.CourseForm(request.POST)
			if form.is_valid():
				in_university_name = request.GET.get('name', 'None')
				in_university = models.University.objects.get(name__exact=in_university_name)
				if in_university.course_set.filter(tag__exact=form.cleaned_data['tag']).exists():
					return render(request, 'courseform.html', {'error' : 'Error: That course tag already exists at this university!'})
				new_course = models.Course(tag=form.cleaned_data['tag'],
										   name=form.cleaned_data['name'],
										   description=form.cleaned_data['description'],
										   university=in_university)
				new_course.save()
				in_university.course_set.add(new_course)
                
				return renderUniversity(request, in_university)
			else:
				return render(request, 'courseform.html', {'error' : 'Undefined Error!'})
		else:
			form = forms.CourseForm()
			return render(request, 'courseform.html')
		# render error page if user is not logged in
	return render(request, 'autherror.html')
		
def removeCourse(request):
	if request.user.is_authenticated():
		in_university_name = request.GET.get('name', 'None')
		in_university = models.University.objects.get(name__exact=in_university_name)
		in_course_tag = request.GET.get('course', 'None')
		in_course = in_university.course_set.get(tag__exact=in_course_tag)
		in_course.delete()
		
        return renderUniversity(request, in_university)
	# render error page if user is not logged in
	return render(request, 'autherror.html')

def joinCourse(request):
    if request.user.is_authenticated():
        in_university_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_university_name)
        in_course_tag = request.GET.get('course', 'None')
        in_course = in_university.course_set.get(tag__exact=in_course_tag)
        
        if (request.user.is_student):
            request.user.student.courses.add(in_course)
            in_course.student_set.add(request.user.student)
        elif (request.user.is_teacher):
            request.user.teacher.courses.add(in_course)
            in_course.teacher_set.add(request.user.teacher)
        request.user.save()
        in_course.save()
        return renderCourse(request, in_course, in_university)
    return render(request, 'autherror.html')

def unjoinCourse(request):
    if request.user.is_authenticated():
        in_university_name = request.GET.get('name', 'None')
        in_university = models.University.objects.get(name__exact=in_university_name)
        in_course_tag = request.GET.get('course', 'None')
        in_course = in_university.course_set.get(tag__exact=in_course_tag)
        
        if (request.user.is_student):
            request.user.student.courses.remove(in_course)
            in_course.student_set.remove(request.user.student)
        elif (request.user.is_teacher):
            request.user.teacher.courses.remove(in_course)
            in_course.teacher_set.remove(request.user.teacher)
        request.user.save()
        in_course.save()
        return renderCourse(request, in_course, in_university)
    return render(request, 'autherror.html')
