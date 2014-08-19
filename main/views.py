from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from main.models import Post


def index(request):

    posts = Post.objects.filter(is_published=True)

    return render_to_response("index.html", {
        "posts": posts
    }, RequestContext(request))


def post_detail(request, slug):

    post = get_object_or_404(Post, slug=slug)

    return render_to_response("detail.html", {
        "post": post
    }, RequestContext(request))