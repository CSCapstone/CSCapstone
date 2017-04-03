"""
UniversitiesApp Views

Created by Jacob Dunbar on 11/5/2016.
"""
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from . import forms
from . import models

from watson import search as watson

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

@login_required
def getUniversities(request):    
    universities_list = models.University.objects.all()
    return render(request, 'universities.html', {'universities': universities_list})

@login_required
def getUniversity(request, slug=''):
    try:
        in_university = models.University.objects.get(slug=slug)
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
    except models.University.DoesNotExist:
        in_university = watson.filter(models.University, slug)   
        context = {
            'universities' : in_university,
        }  
        print slug
        print in_university
        return render(request, 'universities.html', context)

@login_required
def editUniversity(request, slug=''):
    if (slug == ''): # Create New University
        university = models.University(name='')
    else: # Edit Existing Project
        university = models.University.objects.get(slug=slug)

    form = forms.UniversityForm(data=request.POST or None, files=request.FILES or None, instance=university)    
    if request.method == 'POST':
        if form.is_valid():
            university.save()
            messages.success(request, 'Success! Saved university: '+university.name)
            return redirect(reverse('university',kwargs={'slug':university.slug}))

    return render(request, 'universityform.html', { 'university':university, 'form':form })    

@login_required
def joinUniversity(request, slug=''):
    in_university = models.University.objects.get(slug=slug)

    if (request.user.is_student):
        #Making sure this user is not a part of another university
        if (request.user.student.university is not None):                     
            request.user.student.university.student_set.remove(request.user.student)
            request.user.student.university = None
        #Adding this user to this university
        request.user.student.university = in_university
        in_university.student_set.add(request.user.student)

    if (request.user.is_teacher):
        #Making sure this user is not a part of another university
        if (request.user.teacher.university is not None):
            request.user.teacher.university.teacher_set.remove(request.user.teacher)
            request.user.teacher.university = None
        #Adding this user to this university
        request.user.teacher.university = in_university
        in_university.teacher_set.add(request.user.teacher)

    request.user.save()
    in_university.save()

    messages.success(request, 'Success: Joined University!')
    return redirect(reverse('university',kwargs={'slug':in_university.slug}))
 
@login_required   
def unjoinUniversity(request, slug=''):
    in_university = models.University.objects.get(slug=slug)

    if (request.user.is_student and request.user.student.university == in_university):
        in_university.student_set.remove(request.user.student)
        request.user.student.university = None

    if (request.user.is_teacher and request.user.teacher.university == in_university):
        in_university.teacher_set.remove(request.user.teacher)
        request.user.teacher.university = None

    request.user.save()
    in_university.save()
    
    messages.success(request, 'Success: Unjoined University!')
    return redirect(reverse('university',kwargs={'slug':in_university.slug}))


@login_required
def getCourses(request):
    courses = None
    if request.user.is_teacher:
        courses = request.user.teacher.courses.all()
    elif request.user.is_student:
        courses = request.user.student.courses.all()
    context = {
        'courses' : courses,
	}
    return render(request, 'courses.html', context)

@login_required
def getCourse(request, id):
    print "GETTING COURSE"
    in_course = models.Course.objects.get(id=id)
    is_member = False
    if (request.user.is_student and in_course.student_set.filter(user=request.user.student).exists()):
        is_member = True
    elif (request.user.is_teacher and in_course.teacher_set.filter(user=request.user.teacher).exists()):
        is_member = True
    context = {
		'university' : in_course.university,
        'course' : in_course,
		'userIsMember' : is_member,
	}
    return render(request, 'course.html', context)

@login_required
def editCourses(request, id=-1):
    if (id == -1): # Create New Course
        course = models.Course(name='')
    else: # Edit Existing Course
        course = models.Course.objects.get(id=id)

    form = forms.CourseForm(request.POST or None, instance=course)
    if request.method == 'POST':
        if form.is_valid():
            course.university = request.user.teacher.university
            #course.teacher_s.add(request.user)
            form.save()
            #if course == None:
            request.user.teacher.courses.add(course)
            request.user.teacher.save()
            messages.success(request, 'Success! Saved course: '+course.name)
            return render (request, 'course.html', { 'course':course, 'form':form, 'userIsMember':True })
            #return redirect(reverse('course',kwargs={'id':course.id}))

    return render(request, 'courseform.html', { 'course':course, 'form':form })  

@login_required
def joinCourse(request, id):
    course = models.Course.objects.get(id=id)
    if (request.user.is_student):
        request.user.student.courses.add(course)
    elif (request.user.is_teacher):
        request.user.teacher.courses.add(course)
    request.user.save()
    return render(request, 'course.html', { 'course':course, 'userIsMember':True })

@login_required
def unjoinCourse(request, id):
    course = models.Course.objects.get(id=id)
    courses = None
    if (request.user.is_student):
        request.user.is_student.courses.remove(course)
        courses = request.user.student.courses.all()
    elif (request.user.is_teacher):
        request.user.teacher.courses.remove(course)
        courses = request.user.teacher.courses.all()
    request.user.save()
    return render(request, 'courses.html', { 'courses':courses})

@login_required
def deleteCourse(request, id):
    course = models.Course.objects.get(id=id)
    course.delete()
    courses = None
    if (request.user.is_student):
        courses = request.user.student.courses.all()
    elif (request.user.is_teacher):
        courses = request.user.teacher.courses.all()
    return render(request, 'courses.html', { 'courses':courses})

@login_required
def addCourseMember(request, id):
    course = models.Course.objects.get(id=id)
    return render(request, 'addcoursemember.html', { 'course' : course, })

@login_required
def addMemberSuccess(request, id):
    course = models.Course.objects.get(id=id)
    if request.method == 'POST':
        form = forms.CourseMemberForm(request.POST)
        if form.is_valid():
            in_user = models.Student.objects.filter(email__exact=form.cleaned_data['email'].first())
            if not in_user:
                context = {
                    'course' : course,
                    'error' : 'Error, user does not exist!',
                }
                return render(request, 'addcoursemember.html', context)
            if (in_user.is_student):
                in_user.student.courses.add(course)
            elif (in_user.is_teacher):
                in_user.teacher.courses.add(course)
            request.user.save()
            return render(request, 'addcoursemember.html', { 'course' : course, })
        else:
            form = forms.CourseMemberForm()
        return render(request, 'addcoursemember.html')
    return render(request, 'accessdenied.html')

# @login_required
# def getCourse(request, slug=''):	  
# 	in_course = models.Course.objects.get(slug=slug)
#     #TODO: ERROR Checking
# 	return renderCourse(request, in_course, in_course.university)

# @login_required
# def getCourses(request, slug=''):    
#     in_university = models.University.objects.get(slug=slug)
#     in_course = in_university.course_set.all()
#     #TODO: ERROR Checking
#     return renderCourse(request, in_course, in_course.university)


# def courseForm(request):
# 	if request.user.is_authenticated():
# 		in_university_name = request.GET.get('name', 'None')
# 		in_university = models.University.objects.get(name__exact=in_university_name)
# 		context = {
# 			'university': in_university,
# 		}
# 		return render(request, 'courseform.html', context)
#     # render error page if user is not logged in
# 	return render(request, 'autherror.html')

# def addCourse(request):
# 	if request.user.is_authenticated():
# 		if request.method == 'POST':
# 			form = forms.CourseForm(request.POST)
# 			if form.is_valid():
# 				in_university_name = request.GET.get('name', 'None')
# 				in_university = models.University.objects.get(name__exact=in_university_name)
# 				if in_university.course_set.filter(tag__exact=form.cleaned_data['tag']).exists():
# 					return render(request, 'courseform.html', {'error' : 'Error: That course tag already exists at this university!'})
# 				new_course = models.Course(tag=form.cleaned_data['tag'],
# 										   name=form.cleaned_data['name'],
# 										   description=form.cleaned_data['description'],
# 										   university=in_university)
# 				new_course.save()
# 				in_university.course_set.add(new_course)
                
# 				return renderUniversity(request, in_university)
# 			else:
# 				return render(request, 'courseform.html', {'error' : 'Undefined Error!'})
# 		else:
# 			form = forms.CourseForm()
# 			return render(request, 'courseform.html')
# 		# render error page if user is not logged in
# 	return render(request, 'autherror.html')
		
# def removeCourse(request):
# 	if request.user.is_authenticated():
# 		in_university_name = request.GET.get('name', 'None')
# 		in_university = models.University.objects.get(name__exact=in_university_name)
# 		in_course_tag = request.GET.get('course', 'None')
# 		in_course = in_university.course_set.get(tag__exact=in_course_tag)
# 		in_course.delete()
		
#         return renderUniversity(request, in_university)
# 	# render error page if user is not logged in
# 	return render(request, 'autherror.html')

# def joinCourse(request):
#     if request.user.is_authenticated():
#         in_university_name = request.GET.get('name', 'None')
#         in_university = models.University.objects.get(name__exact=in_university_name)
#         in_course_tag = request.GET.get('course', 'None')
#         in_course = in_university.course_set.get(tag__exact=in_course_tag)
        
#         if (request.user.is_student):
#             request.user.student.courses.add(in_course)
#             in_course.student_set.add(request.user.student)
#         elif (request.user.is_teacher):
#             request.user.teacher.courses.add(in_course)
#             in_course.teacher_set.add(request.user.teacher)
#         request.user.save()
#         in_course.save()
#         return renderCourse(request, in_course, in_university)
#     return render(request, 'autherror.html')

# def unjoinCourse(request):
#     if request.user.is_authenticated():
#         in_university_name = request.GET.get('name', 'None')
#         in_university = models.University.objects.get(name__exact=in_university_name)
#         in_course_tag = request.GET.get('course', 'None')
#         in_course = in_university.course_set.get(tag__exact=in_course_tag)
        
#         if (request.user.is_student):
#             request.user.student.courses.remove(in_course)
#             in_course.student_set.remove(request.user.student)
#         elif (request.user.is_teacher):
#             request.user.teacher.courses.remove(in_course)
#             in_course.teacher_set.remove(request.user.teacher)
#         request.user.save()
#         in_course.save()
#         return renderCourse(request, in_course, in_university)
#     return render(request, 'autherror.html')
