from django.shortcuts import render
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User

# Create your views here.

# APIView->mixins.CRUDModelMixin->generics.CRUDAPIView

class SnippetList(generics.ListCreateAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

	#save with foreign key to database
	def perform_create(self, serializer):
		serializer.save(owner = self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	# it could be other fields of Snippet model, 
	# we use pk here, in accordance with url(r'^/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()), in urls.py
	lookup_field = 'pk'

'''
class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = SnippetSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = SnippetSerializer
	'''
