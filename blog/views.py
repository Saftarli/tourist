from django.shortcuts import render, get_object_or_404

from blog.models import Blog


# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from blog.models import Blog

def blog(request):
    blog_list = Blog.objects.all().order_by('-created')
    paginator = Paginator(blog_list, 4)  # hər səhifədə 4 xəbər

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'blog': page_obj,
        'page_obj': page_obj
    }
    return render(request, 'blog/blog.html', context)

def blog_detail(request, slug):
    context = {
        'blog': get_object_or_404(Blog, slug=slug),
        'request': request,
    }
    return  render(request,'blog/blog-details.html', context)
