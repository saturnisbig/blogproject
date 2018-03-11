#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django import forms

from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'email', 'url', 'content']

