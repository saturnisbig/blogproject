#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django import template

from comments.models import PostComment


register = template.Library()


@register.simple_tag
def get_comment_count(post):
    comment_list = post.post_comments.all()
    return len(comment_list)


@register.simple_tag
def get_comment_author_count(post):
    comment_list = post.post_comments.all()
    author_list = []
    for comment in comment_list:
        author = comment.author
        if author not in author_list:
            author_list.append(author)
    return len(author_list)


@register.simple_tag
def get_parent_comment(post):
    comment_list = post.post_comments.filter(parent=None)
    return comment_list


@register.simple_tag
def get_child_comment(com):
    com_list = com.postcomment_child_comments.all()
    return com_list

@register.simple_tag
def get_recent_comments(num=5):
    recent_cmt_list = PostComment.objects.all()[:num]
    return recent_cmt_list
