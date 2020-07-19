from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog, Comment
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from django.contrib import messages
# from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
# def index(request):


#     data= Blog.objects.all().order_by('-date_posted')


#     return render(request, 'index.html', {'data':data})


class BlogListView(ListView):
    model= Blog
    template_name='blog.html'
    context_object_name='data'
    ordering= ['-date_posted']
    paginate_by= 3

@login_required(login_url="/account/signin" )
def create_blog(request):
    
    if request.method=='POST':
        title=request.POST['title']
        writer=request.POST['writer']
        content=request.POST['content']
        img=request.FILES['img']
        data=Blog(title=title,content=content,img=img, writer=writer)
        
        data.save()
        print("data saved")
        
        return redirect('/')

    else:
        
      
        return render(request, 'create_blog.html')
      

    
    

def blog_details(request,id):

    detail= Blog.objects.get(id=id)

    return render (request, 'blog_detail.html', {'detail':detail})

def edit_blog(request, id):

    edit= Blog.objects.get(id=id)
    if request.method=="POST":
        edit.title= request.POST['title']
        edit.writer= request.POST['writer']
        edit.content= request.POST['content']
        edit.img= request.FILES['img']
        edit.save()
        return redirect('/')

    else:
        return render(request, 'edit_blog.html', {'edit':edit})

def delete_blog(request, id):
    delt= Blog.objects.get(id=id)
    delt.delete()
    return redirect('/')


    
    
def search(request):
    if request.method=="POST":
        search=request.POST['search']
        if search:
                  data= Blog.objects.filter(Q(title__icontains=search))
                  if data:
                    return render(request, 'search.html', {'sr':data})
                  else:
                     messages.error(request, 'no result found')
                     return redirect('/')

        else:
            return HttpResponseRedirect("/search/")


    else:
        return render(request, 'search.html')
        #this 




def comment(request, id):
    if request.method=='POST':
        comment=request.POST['comment']

        com=Comment(comment=comment)
        com.save()
        return redirect('/')
    else:
        com=Comment.objects.get(id=id)
        print("data retriving.")
        return render(request, 'blog_detail.html', {'com':com})
        


