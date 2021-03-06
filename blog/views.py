# -*- coding: utf-8 -*-

import markdown
from markdown.extensions.toc import TocExtension
import time

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.utils.text import slugify
from django.conf import settings

from blog.models import Entry, Category, Tag
from comments.forms import PostCommentForm
# from tools import remove_markdown_toc


class IndexView(ListView):
    model = Entry
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = settings.ENTRY_PER_PAGE

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        pagination_data = self.pagination_data(is_paginated, paginator, page)
        context.update(pagination_data)
        return context

    def pagination_data(self, is_paginated, paginator, page, per_page=2):
        if not is_paginated:
            return {}
        first = False
        last = False
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        page_number = page.number
        total_pages = paginator.num_pages
        page_range = list(paginator.page_range)

        if page_number == 1:
            right = page_range[page_number:(page_number+per_page)]
            if right[-1] < total_pages - 1:
                right_has_more = True

            if right[-1] < total_pages:
                last = True
        elif page_number == total_pages:
            # index in page_range
            index = total_pages - 1
            left_start = index - per_page
            left = page_range[(left_start) if left_start > 0 else 0:index]
            if left[0] > 2:
                left_has_more = True

            if left[0] > 1:
                first = True
        else:
            index = page_number - 1
            left_start = index - per_page
            left = page_range[left_start if left_start > 0 else 0:index]
            right = page_range[page_number:page_number+per_page]
            if left[0] > 2:
                left_has_more = True

            if left[0] > 1:
                first = True

            if right[-1] < total_pages - 1:
                right_has_more = True

            if right[-1] < total_pages:
                last = True

        return {
            'first': first,
            'left': left,
            'left_has_more': left_has_more,
            'right': right,
            'right_has_more': right_has_more,
            'last': last,
        }


class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        cate = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        context['current_obj'] = cate
        context['current_title'] = '文章分类'
        return context

    def get_queryset(self):
        cate = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


class ArchiveView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchiveView, self).get_queryset().filter(
            c_time__year=year,
            c_time__month=month)

def archives_list(request):
    return render(request, 'blog/archives.html')


class EntryDetailView(DetailView):
    model = Entry
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(EntryDetailView, self).get(request, *args, **kwargs)
        # self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        post = super(EntryDetailView, self).get_object(queryset=queryset)
        u = self.request.user
        ses = self.request.session
        the_key = 'is_read_{}'.format(post.id)
        if u != post.author:
            last_visit_time = ses.get(the_key)
            if not last_visit_time:
                post.increase_views()
                ses[the_key] = time.time()
            else:
                now_time = time.time()
                del_t = now_time - last_visit_time
                if del_t > 60 * 30:
                    post.increase_views()
                    ses[the_key] = time.time()
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            # 支持中文锚点
            TocExtension(slugify=slugify)]
            # 'markdown.extensions.toc']
        )
        # post.body = remove_markdown_toc(md.convert(post.body))
        post.body = md.convert(post.body)
        post.toc = md.toc
        return post

    def get_context_data(self, **kwargs):
        context = super(EntryDetailView, self).get_context_data(**kwargs)
        form = PostCommentForm()
        # comment_list = self.object.post_comments.all()
        context.update({
            'form': form,
            # 'comment_list': comment_list
        })
        return context


class TagView(IndexView):
    # 为了在模板显示标签名
    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        context['current_obj'] = tag
        context['current_title'] = '文章标签'
        return context

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag)


class PopularView(IndexView):
    def get_queryset(self):
        return super(PopularView, self).get_queryset().order_by('-views')


def index(request):
    post_list = Entry.objects.all()
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def detail(request, pk):
    post = get_object_or_404(Entry, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    post.increase_views()
    form = PostCommentForm()
    comment_list = post.comment_set.all()
    context = {'post': post,
               'comment_list': comment_list,
               'form': form}
    return render(request, 'blog/detail.html', context)


def archives(request, year, month):
    post_list = Entry.objects.filter(c_time__year=int(year),
                                     c_time__month=int(month))
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Entry.objects.filter(category=cate)
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)
