"""
UniversitiesApp Models

Created by Jacob Dunbar on 11/5/2016.
"""
from django.db import models
from django.utils.text import slugify
from AuthenticationApp.models import MyUser

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="static/universityimages", default=0)
    description = models.CharField(max_length=300, default="")
    website = models.CharField(max_length=300, default="")

    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    # 	if not self.id:
    # 		# Newly created object, so set slug            
	   #  	original = slugify(self.name)	    	
	   #  	#Checking if slug is unique
	   #  	if University.objects.filter(slug=original).exists():	 
	   #  		in_university = University.objects.get(slug=original)
	   #  		#Make new slug by combining name and id of previous instance
	   #      	self.slug = slugify('%s-%d' % (original, in_university.id))
	   #      else:
	   #      	self.slug = original

    #     super(University, self).save(*args, **kwargs)
	
class Course(models.Model):
	tag = models.CharField(max_length=10)
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=300)
	website = models.CharField(max_length=300, default="")
	university = models.ForeignKey(University, related_name='course_set', on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.name			