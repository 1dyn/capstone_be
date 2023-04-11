from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import User, Scholarship
from datetime import datetime
import datetime


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=["name", "age"],
            )
        ]


class ScholarshipSerializer(serializers.ModelSerializer):
    d_day = serializers.SerializerMethodField()

    class Meta:
        model = Scholarship
        fields = [
            "id",
            "title",
            "institution",
            "type",
            "benefit",
            "target",
            "start_date",
            "end_date",
            "view_num",
            "d_day",
        ]
        validators = [
            UniqueTogetherValidator(
                queryset=Scholarship.objects.all(),
                fields=["title", "start_date", "end_date"],
            )
        ]

    def get_d_day(self, obj):
        d_day = (obj.end_date - datetime.datetime.now().date()).days
        if int(d_day) < 0:
            return -1
        else:
            return d_day
