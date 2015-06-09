# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

 #Views for journal
 
def students_journal(request):
    return render(request, 'students/journal.html',{})
