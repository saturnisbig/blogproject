# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from tool.models import CardID


def index(request):
    return render(request, 'tool/index.html')


def webcolor(request):
    return render(request, 'tool/webcolor.html')


@require_POST
def convert_color(request):
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
    rgb = list(int(v) for v in value.split(','))
    print(rgb)
    if len(rgb) != 3 or rgb[0] > 255 or rgb[1] > 255 or rgb[2] > 255:
        return ''
    r = '#%02x%02x%02x' % (rgb[0], rgb[1], rgb[2])
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
def get_cardid(request):
    msg = '查询失败'
    ret = {}
    if request.is_ajax():
        data = request.POST
        idnumber = data.get('cardid')
        if len(idnumber) > 6:
            idnumber = idnumber[:7]
        # try:
            # cardid = CardID.objects.get(number=idnumber)
        # except CardID.DoesNotExist:
        #     cardid = None
        cardid = get_object_or_404(CardID, number=idnumber)
        # 获取所属省份
        province_number = idnumber[:2] + '0000'
        province = get_object_or_404(CardID, number=province_number)
        # 获取所属城市
        city_number = idnumber[:4] + '00'
        city = get_object_or_404(CardID, number=city_number)
        place = ''
        if province:
            place = province.place
        if city:
            place = place + ',' + city.place
        if not cardid:
            msg = '未找到，请检查输入！'
        else:
            ret['number'] = cardid.number
            ret['place'] = place + ',' + cardid.place
            ret['msg'] = '查询成功'
            return JsonResponse(ret)
    ret['msg'] = msg
    return JsonResponse(ret)


@require_POST
def get_cardname(request):
    msg = '查询失败'
    ret = {}
    if request.is_ajax():
        data = request.POST
        idname = data.get('cardname')
        # 一个地方可能有新旧号
        cards = CardID.objects.filter(place__icontains=idname)
        # 获取所属省份
        if not cards:
            msg = '未找到，请检查输入！'
        else:
            province_number = cards[0].number[:2] + '0000'
            province = get_object_or_404(CardID, number=province_number)
            ret['cards'] = []
            place = ''
            for card in cards:
                if province:
                    place = province.place
                city_number = card.number[:4] + '00'
                city = get_object_or_404(CardID, number=city_number)
                if city:
                    place = place + ',' + city.place
                place = place + ',' + card.place
                ret['cards'].append({'number': card.number,
                                     'place': place})
            ret['msg'] = '查询成功'
            # print ret
            return JsonResponse(ret)
    ret['msg'] = msg
    return JsonResponse(ret)
