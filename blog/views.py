from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from blog.models import Post
from creoleparser import text2html


def blog(request, post_id=None):
    context = RequestContext(request)
    if post_id is None:
        posts_data = []
        posts = Post.objects.all().order_by('-created_time')[:5]
        for post in posts:
            post_datum = {}
            post_datum['post'] = post
            post_datum['parsed'] = text2html(post.content)
            posts_data.append(post_datum)
        context['posts_data'] = posts_data
        return render_to_response('blog/main.html', context)
    else:
        try:
            post_obj = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            post_obj = None
        if post_obj is not None:
            context['post'] = post_obj
            context['parsed'] = text2html(post_obj.content)
            return render_to_response('blog/post.html', context)
        else:
            return HttpResponse('Post Not Found!')
