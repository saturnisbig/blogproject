# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect

from blog.models import Entry
from .forms import CommentForm


def post_comment(request, post_pk):
    post = get_object_or_404(Entry, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = post
            form.save()
            # 调用Entry的get_absolute_url方法
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {
                'post': post,
                'form': form,
                'comment_list': comment_list,
            }
            return render(request, 'blog/detail.html', context)
    return redirect(post)
