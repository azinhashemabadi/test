from rest_framework import serializers
from .models import Measurement,Ping,DNS,Download,Upload,Web
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'  

class PingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ping
        fields = '__all__'  

class DNSSerializer(serializers.ModelSerializer):
    class Meta:
        model = DNS
        fields = '__all__'    

class DownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Download
        fields = '__all__'      

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = '__all__'      
class WebSerializer(serializers.ModelSerializer):
    class Meta:
        model = Web
        fields = '__all__'      
