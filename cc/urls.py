from .views import CreateMeasurement,GetAllMeasurements,CustomObtainPairView,measurement_geojson
from django.urls import path


urlpatterns = [
        path('measurements/', CreateMeasurement.as_view(), name='create_measurement'),
        path('measurements/all/', GetAllMeasurements.as_view(), name='get_all_measurements'),
        path("jwt/create/", CustomObtainPairView.as_view(), name="customtoken"),
        path('signal-map/', measurement_geojson , name='measurement-geojson'),
]