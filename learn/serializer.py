from rest_framework import serializers
from models import signup_model
class sighn_serializer(serializers.ModelSerializer):
    class meta:
        model = signup_model
        fields = '__all__'
