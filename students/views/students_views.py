# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

	#Views for Student

def students_list(request):
	students = (
	{'id': 1,
	'first_name': u'Віталій',
	'last_name': u'Подоба',
	'ticket': 235,
	'image': 'img/garage-sale_c1.jpg'},
	{'id': 2,
	'first_name': u'Притула',
	'last_name': u'Анастасия',
	'ticket': 2123,
	'image': 'img/image1.png'},
	{'id': 3,
	'first_name': u'Леус',
	'last_name': u'Володимир',
	'ticket': 212,
	'image': 'img/garage_sale_t.jpg'},
	)
	return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
	return render(request, 'students/students_add.html', {})

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)	