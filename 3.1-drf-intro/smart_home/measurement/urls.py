from django.urls import path, include
from measurement.views import SensorsView, MeasurementView
from rest_framework import routers


router = routers.DefaultRouter()
router.register('sensors', SensorsView)
router.register('measurements', MeasurementView)

urlpatterns = [
    path('', include(router.urls))
]
