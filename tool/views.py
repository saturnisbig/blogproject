# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse


def index(request):
    return render(request, 'tool/index.html')


def webcolor(request):
    return render(request, 'tool/webcolor.html')


@require_POST
def convert_color(request):
    print 'here'
    result = ''
    msg = '转换失败, 检查输入值格式'
    ret = {}
    if request.is_ajax():
        data = request.POST
        t = data.get('convert_type')
        value = data.get('color')
        ret['base_color'] = value
        if t == '2hex':
            result = to_hex(value)

        if t == '2rgb':
            result = to_rgb(value)
        if result:
            msg = '转换成功'
        else:
            msg = '转换失败,请检查数据输入格式'
    ret['msg'] = msg
    ret['result'] = result
    return JsonResponse(ret)


def to_hex(value):
    if value.startswith('rgb(') and value.endswith(')'):
        value = value[4:-1]
    if value.startswith('(') and value.endswith(')'):
        value = value[1:-1]
    r, g, b = (int(v) for v in value.split(','))
    if r > 255 or b > 255 or g > 255:
        return ''
    r = '#%02x%02x%02x' % (r, g, b)
    return r.upper()


def to_rgb(value):
    if value[0] != '#' or len(value) != 7:
        return ''
    else:
        r, g, b = value[1:3], value[3:5], value[5:7]
        return '%s, %s, %s' % (int(r, 16), int(g, 16), int(b, 16))

def id_place(request):
    return render(request, 'tool/idplace.html')


@require_POST
def getid(request):
    pass
