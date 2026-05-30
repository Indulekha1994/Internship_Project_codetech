from rest_framework import serializers
from .models import WebsiteUsage

class WebsiteUsageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WebsiteUsage
        fields = '__all__'