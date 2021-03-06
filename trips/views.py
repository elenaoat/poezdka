#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, Http404
from . import models


def index(request):
	posts = models.Post.objects.order_by('-pub_date')[:3]
	ctx = {'posts': posts}
	template = 'trips/index.html'
	return render(request, template, ctx)

def post(request, slug):
	try:
		p = models.Post.objects.get(slug=slug)
	except models.Post.DoesNotExist:
		raise Http404('Such post does not exist.')
	template = 'trips/post.html'
	latest = models.Post.objects.all().order_by('-pub_date')

	ctx = {'post': p, 'latest': latest[:3], 'other': latest[3:]}
	return render(request, template, ctx)

def about(request):
	ctx = {}
	template = 'trips/about.html'
	return render(request, template, ctx)