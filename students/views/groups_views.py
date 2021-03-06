# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

#Views for Groups

def groups_list(request):
	groups = (
		{'id': 1,
		'starosta': u"Леус Володимир",
		'name': u"МтМ-21"},
		{'id': 2,
		'starosta': u"Притула Анастасія",
		'name': u"МтМ-22"},
		{'id': 3,
		'starosta': u"Віталій Подоба",
		'name': u"МтМ-23"},
		)
	return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)