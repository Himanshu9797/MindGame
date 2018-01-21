from django.shortcuts import render
from django.contrib.auth import authenticate, login

from rest_framework import status
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

class AppUserlogin(APIView):
	def post(self, request):
		params = request.data
		user = authenticate(email=params['email'], password=params['password'])
		if user:
			login(request,user)
			serializer = AppUserSerializer(user)
			return Response({"message":"You have sucessfully logged in.","user":serializer.data},
			 status = status.HTTP_200_OK)

		else:
			return Response({"message":"Please enter valid credentials."}, status=status.HTTP_404_NOT_FOUND)
