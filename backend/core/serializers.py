from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField



class ContactSerializer(serializers.ModelSerializer): 
	# Create a new class that links to the model

	name = CharField(source="title", required=True) 
	# source is the name of the field in the model
	message = CharField(source="description", required=True)
	# required is the field required to be filled
	email = EmailField(required=True)
	
	class Meta:
		model = models.Contact
		fields = (
			'name',
			'email',
			'message'
		)