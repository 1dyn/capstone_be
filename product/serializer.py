from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import User, Scholarship

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['name', 'age'],
            )
        ]

class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholarship
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Scholarship.objects.all(),
                fields=['title', 'start_date', 'end_date'],
            )
        ]
