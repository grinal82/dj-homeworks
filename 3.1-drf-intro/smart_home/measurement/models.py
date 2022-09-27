from tkinter import CASCADE
from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):

    name = models.CharField(max_length=40, verbose_name='имя датчика')
    description = models.CharField(max_length=50, verbose_name='описание')

    class Meta:
        verbose_name = "Датчик"
        verbose_name_plural = "Датчики"

    def __str__(self):
        return self.name
    
class Measurement(models.Model):
        
    temperature = models.FloatField(verbose_name="температура")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'дата')
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Измерение"
        verbose_name_plural = 'Измерения'
        ordering = ['-created_at']

