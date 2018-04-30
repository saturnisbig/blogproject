#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from django import forms

from .models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['site_url', 'avatar']
