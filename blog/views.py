from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from blog.models import Post
from creoleparser import text2html


def blog(request, post_id=None):
    context = RequestContext(request)
    if post_id is None:
        post_list = Post.objects.all()
        context['posts'] = post_list
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
