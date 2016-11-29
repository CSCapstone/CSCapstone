from . import forms
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Comment,SubComment
#from . import forms
from django.core.urlresolvers import reverse_lazy


# Create your views here.
def getComments(request):
    comment_list = Comment.objects.all()
    context = {
        'comment' : comment_list,
    }
    return render(request,'comments.html',context)
    #return HttpResponse("Hello, world. You're at the polls index.")

def getCommentForm(request):
    return render(request, 'commentForm.html')

def addComment(request):
    print("i am in addcomment")
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comment(comment=form.cleaned_data['comment'])
            new_comment.save()
            comments_list = Comment.objects.all()
            context = {
                'comment' : comments_list,
            }
            return render(request, 'comments.html', context)
        else:
            form = forms.CommentForm()
    return render(request, 'comments.html')

def addSubComment(request,comment_id):
    print(request.POST['subcomment'])
    subcomment = request.POST['subcomment']

    c = Comment.objects.get(pk=comment_id)
    #parent_comment.subcomment_set.create(comment=subcomment)
   # parent_comment.save()
    new_subcomment = SubComment(parent_comment=c,comment=subcomment)
    new_subcomment.save()
    #parent_comment.subcomment_set.add(new_subcomment)
    return redirect('comment:Comments')
    #return render(request,'comments.html')
    #new_subcomment = SubComment()

    #return HttpResponse("i belive u just send this value " + request.POST['subcomment'])

