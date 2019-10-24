from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from blog.models import Blog,User,Comment

# Create your views here.
def Post(request,b_id):
    if request.method == 'GET':
        blog = Blog.objects.filter(b_id=b_id).first()
        blogobj = Blog.objects.all()
        comments = Comment.objects.filter(blogobj=b_id).all()
        # userobj = User.objects.filter(userobj=1)
        return render(request,'post.html',locals())
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        comment = request.POST.get("comment")
        # print(username,email,comment)
        blogobj = Blog.objects.filter(b_id=b_id).first()
        blogobj.commentcount += 1
        blogobj.save()
        user = User.objects.filter(u_name=username, u_email=email).first()
        # print(user.u_id)
        if user:
            Comment.objects.create(content=comment, userobj=user, blogobj=blogobj)
        else:
            User.objects.create(u_name=username,u_email=email)
            user = User.objects.filter(u_name=username, u_email=email).first()
            Comment.objects.create(content=comment, userobj=user, blogobj=blogobj)
        return redirect('/post/%s'%(b_id))

def Index(request):
    if request.method == "GET":
        blogobj = Blog.objects.all()
        return render(request,'index.html',{'blogobj':blogobj})

def Blogs(request):
    if request.method == 'GET':
        blogobj = Blog.objects.all()
        # return render(request,'blog.html',{'blogobj':blogobj})

        # book_list = Book.objects.all()
        paginator = Paginator(blogobj, 2)
        current_page_num = int(request.GET.get('page', 1))
        if paginator.num_pages > 11:
            if current_page_num - 5 < 1:
                page_range = range(1, 12)
            elif current_page_num + 5 > paginator.num_pages:
                page_range = range(paginator.num_pages - 10, paginator.num_pages + 1)
            else:
                page_range = range(current_page_num - 5, current_page_num + 6)
        else:
            page_range = paginator.page_range
        try:
            current_page = paginator.page(current_page_num)
        except EmptyPage as e:
            current_page = paginator.page(1)
        return render(request,'blog.html', locals())