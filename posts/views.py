from django.shortcuts import render

try:
    from posts.models import Post
except Exception:
    Post = None


# Create your views here.
def show_post_detail(request, pk):
    if Post:
        post = Post.objects.get(pk=pk)
    else:
        post = None
    context = {
        "post": post,
    }
    return render(request, "posts/detail.html", context)


def list_all_posts(request):
    if Post:
        posts = Post.objects.all()
    else:
        posts = None
    context = {
        "posts": posts,
    }
    return render(request, "posts/list.html", context)
