from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from .serializers import AppUserSerializer
from .models import AppUser
# Create your views here.

class signup(CreateAPIView):
	queryset = AppUser.objects.all()
	serializer_class = AppUserSerializer
	parser_classes = (JSONParser, FormParser, MultiPartParser)

class signup1(APIView):
	def post(self,request):
		print(request.POST)
		return Response()
