from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse,redirect
from .models import Post,Images
from mycompany.my_function import get_ip_address
from itertools import chain
from django.shortcuts import redirect
# Create your views here.
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def index(request):
    post=Post.objects.all().order_by('-Id')[:3]
    post = {"final": post}
    return render(request,'index.html',post)

def only_three(request):
    post = Post.objects.order_by('pub_date').all()[:3]
    post = {"final": post}
    return render(request, 'test.html', post)

def image_return(request,id):
    temp={}
    chk=Images.objects.filter(note=int(id)).values()
    for i in chk:
        final="media/"+i[['image']]
        temp.append(final)
    return HttpResponse(temp)

def single_return(request,Id):
    blog_id=Id
    print("test",blog_id)
    num=Post.objects.get(Id=blog_id)
    cont={"blog":num}
    return render(request,'complete_blog.html',context=cont)

def blog_return(request):
    post = Post.objects.order_by('pub_date').all()[:1]
    post = {"final": post}
    return HttpResponseRedirect(post)

def blog(request):
    post = Post.objects.all()
    final = {"blog":post}
    return render(request, "Blog.html", context=final)

def contact(request):
    return render(request,'contact.html')

def completeblog(request):
    post = Post.objects.first()
    post = {"final": post}
    return render(request,"complete_blog.html",context=post)

def detail(request):
    return render(request,"details.html")

def redirect_view(request):
    response = redirect('/')
    return response
def redirect_blog(request):
    response = redirect('/blog')
    return response
def redirect_contact(request):
    response = redirect('/contact')
    return response
def redirect_detail(request):
    response = redirect('/details')
    return response