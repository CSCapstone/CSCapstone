from . import forms
from django.shortcuts import render
from django.http import HttpResponse
from . import models
#from . import forms



# Create your views here.
def getComments(request):
    comment_list = models.Comment.objects.all()
    context = {
        'comment' : comment_list,
    }
    return render(request,'comments.html',context)
    #return HttpResponse("Hello, world. You're at the polls index.")

def getCommentForm(request):
    return render(request, 'commentForm.html')

def addComment(request):
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            new_comment = models.Comment(comment=form.cleaned_data['comment'])
            new_comment.save()
            comments_list = models.Comment.objects.all()
            context = {
                'comment' : comments_list,
            }
            return render(request, 'comments.html', context)
        else:
            form = forms.CommentForm()
    return render(request, 'comments.html')
