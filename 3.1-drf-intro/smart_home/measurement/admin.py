from django.contrib import admin

from measurement.models import Measurement, Sensor

# Register your models here.
class MeasurementInline(admin.TabularInline):
    model = Measurement



@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    inlines = [MeasurementInline]
    list_display = ('id', 'name', 'description')

    
@admin.register(Measurement)
class MeasurmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'temperature', 'created_at', 'sensor_id')