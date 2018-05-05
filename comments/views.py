# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from blog.models import Entry
from .models import PostComment


@login_required
@require_POST
def post_comment(request):
    if request.is_ajax():
        data = request.POST
        post_id = data.get('post_id')
        post = get_object_or_404(Entry, pk=post_id)
        new_content = data.get('content')
        rep_id = data.get('rep_id')
        if not rep_id:
            new_comment = PostComment(author=request.user, content=new_content,
                                      parent=None, rep_to=None, post=post)
        else:
            new_rep_to = get_object_or_404(PostComment, pk=int(rep_id))
            new_parent = new_rep_to.parent if new_rep_to.parent else new_rep_to
            new_comment = PostComment(author=request.user, content=new_content,
                                      parent=new_parent, rep_to=new_rep_to,
                                      post=post)
        new_comment.save()
        new_point = '#com-' + str(new_comment.id)
        return JsonResponse({'msg': '评论提交成功!', 'new_point': new_point})
    return JsonResponse({'msg': '评论失败!'})
