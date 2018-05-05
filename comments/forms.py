#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django import forms

from comments.models import PostComment


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['content']
