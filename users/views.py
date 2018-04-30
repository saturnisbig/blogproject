# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def change_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = ProfileForm(instance=request.user)
        return render(request, 'users/change_profile.html', {'form': form})
