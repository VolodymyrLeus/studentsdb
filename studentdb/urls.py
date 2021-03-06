from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # students urls
    url(r'^$', 'students.views.students_views.students_list', name='home'),
    url(r'^students/add/$', 'students.views.students_views.students_add', name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', 'students.views.students_views.students_edit', name='students_edit'),
	url(r'^students/(?P<sid>\d+)/delete/$', 'students.views.students_views.students_delete', name='students_delete'),

    # Groups urls
	url(r'^groups/$', 'students.views.groups_views.groups_list', name='groups'),
	url(r'^groups/add/$', 'students.views.groups_views.groups_add', name='groups_add'),
	url(r'^groups/(?P<gid>\d+)/edit/$', 'students.views.groups_views.groups_edit', name='groups_edit'),
	url(r'^groups/(?P<gid>\d+)/delete/$', 'students.views.groups_views.groups_delete', name='groups_delete'),

	#Journal urls
	url(r'^journal/$', 'students.views.journal_views.students_journal', name='students_journal'),
	
	url(r'^admin/', include(admin.site.urls)),
)
