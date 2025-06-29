import folium
from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from rest_framework.views import APIView
from .serializers import MeasurementSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
class CreateMeasurement(APIView):
    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetAllMeasurements(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        measurements = Measurement.objects.all()
        serializer = MeasurementSerializer(measurements, many=True)
        return Response(serializer.data)   
        
class CustomObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
def get_signal_color(rsrp):
    """Determine color based on RSRP value"""
    if rsrp is None:
        return 'gray'
    if rsrp >= -80:
        return 'green'  # Excellent
    elif rsrp >= -90:
        return 'blue'   # Good
    elif rsrp >= -100:
        return 'orange' # Fair
    else:
        return 'red'    # Poor

def measurement_geojson(request):
    measurements = Measurement.objects.exclude(latitude__isnull=True).exclude(longitude__isnull=True)
    
    features = []
    for measurement in measurements:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [measurement.longitude, measurement.latitude]
            },
            "properties": {
                "device_id": measurement.device_id,
                "rsrp": measurement.rsrp,
                "rsrq": measurement.rsrq,
                "technology": measurement.technology,
                "cell_id": measurement.cell_id,
                "color": get_signal_color(measurement.rsrp),
                "recorded_at": measurement.recorded_at.isoformat()
            }
        })
    
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    
    return JsonResponse(geojson)

class MeasurementListView(APIView):
    def get(self, request):
        measurements = Measurement.objects.all()
        serializer = MeasurementSerializer(measurements, many=True)
        return Response(serializer.data)