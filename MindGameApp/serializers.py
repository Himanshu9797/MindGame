from rest_framework import serializers
from .models import AppUser 


class AppUserSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		obj = AppUser.objects.create(**validated_data)
		obj.set_password(validated_data['password'])
		obj.save()
		return obj

	class Meta:
		model = AppUser
		fields = ('first_name','last_name','email','password')