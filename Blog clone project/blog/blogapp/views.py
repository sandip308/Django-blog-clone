from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from blogapp.models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import Postform,Commentform
from django.urls import reverse_lazy
# Create your views here.

class Aboutview(TemplateView):
    template_name = 'about.html'


class Postlistview(ListView):   #Home page                         
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__lte =timezone.now()).order_by('-published_date')

class Postdetailview(DetailView):
    model = Post

class Createpostview(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blogapp/post_detail.html'
    form_class = Postform
    model = Post

class Postupdateview(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blogapp/post_detail.html'
    form_class = Postform
    model = Post

class Postdeleteview(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list') 
class Postdraftview(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blogapp/post_list.html'
    model = Post
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')
    
###################################### COMMENTS ######################################
@login_required
def add_comment(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = Commentform(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = Commentform()
    return render(request,'blogapp/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)


