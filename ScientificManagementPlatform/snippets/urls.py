from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
	url(r'^$',views.SnippetList.as_view()),
	#url(r'^users/$', views.UserList.as_view()),
	# for function based view
	#url(r'^snippets/(?P<pk>[0-9]+)$',views.snippet_detail),
	# for class based view
	url(r'^(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
	#url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

