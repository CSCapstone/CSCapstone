from django.shortcuts import render
from CommentsApp.models import Comment, Sub_Comment
from . import models

from . import forms


# def getComments(request):
#     return render(request, 'comments.html')


def getCommentForm(request):
    comments_list = list(models.Comment.objects.all())
    # cont = {}
    # for com in comments_list:
    #     cont[com] = Sub_Comment.objects.filter(com.id)

    sub_comment_list = models.Sub_Comment.objects.all()
    context = {
        'comments': comments_list,
    }
    return render(request, 'commentForm.html', context)

def addComment(request):
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            new_comment = models.Comment(comment=form.cleaned_data['comment'])
            new_comment.save()
            comments_list = models.Comment.objects.all()
            context = {
                'comments' : comments_list,
            }
            return render(request, 'comments.html', context)
        else:
            form = forms.CommentForm()
    return render(request, 'comments.html')

def addSubComment(request):
    if request.method == 'POST':
        form = forms.SubCommentForm(request.POST)
        if form.is_valid():
            comment = Comment.objects.filter(id=form.data['id'])
            new_sub_comment = models.Sub_Comment(comment_id=comment, comment=form.cleaned_data['comment'])
            new_sub_comment.save()
            comments_list = models.Comment.objects.all()
            context = {
                'comments' : comments_list,
            }
            return render(request, 'comments.html', context)
        else:
            form = forms.CommentForm()
    return render(request, 'comments.html')

def getComments(request):
    comments_list = models.Comment.objects.all()
    context = {
        'comments' : comments_list,
    }
    return render(request, 'comments.html', context)