from .views import CreateMeasurement,GetAllMeasurements,CustomObtainPairView,measurement_geojson,PingCreateView,DNSCreateView,DownloadCreateView,UploadCreateView,WebCreateView
from django.urls import path


urlpatterns = [
        path('measurements/', CreateMeasurement.as_view(), name='create_measurement'),
        path('measurements/all/', GetAllMeasurements.as_view(), name='get_all_measurements'),
        path("jwt/create/", CustomObtainPairView.as_view(), name="customtoken"),
        path('signal-map/', measurement_geojson , name='measurement-geojson'),
        path('api/ping/', PingCreateView.as_view(), name='ping-create'),
        path('api/dns/', DNSCreateView.as_view(), name='dns-create'),
        path('api/download/', DownloadCreateView.as_view(), name='download-create'),
        path('api/upload/', UploadCreateView.as_view(), name='upload-create'),
        path('api/web/', WebCreateView.as_view(), name='web-create'),
        path('api/webbb/', WebCreateView.as_view(), name='web-create'),
]