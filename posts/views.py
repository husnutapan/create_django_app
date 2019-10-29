from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from posts.forms import PostForm
from posts.models import Post


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Item saved", extra_tags="success-custom")
        return HttpResponseRedirect(instance.get_absolute_path())

    context_data = {
        'form': form
    }
    return render(request, 'post_form.html', context_data)


def post_detail(request, id):
    # instance = Post.objects.get(id=1)
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, "post_detail.html", context)


def post_list(request):
    instance = Post.objects.all()
    context_data = {
        'title': 'List',
        'object_list': instance
    }
    return render(request, 'index.html', context_data)
    # return HttpResponse("<h1>List</h1>")


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    instance = form.save(commit=False)
    instance.save()
    context_data = {
        'form': form
    }
    return render(request, 'post_form.html', context_data)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Deleted successfully..")
    return redirect("list")
