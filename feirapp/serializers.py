from rest_framework import serializers
from feirapp.models import Feira #, LANGUAGE_CHOICES, STYLE_CHOICES


class FeiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feira
        fields = '__all__'
