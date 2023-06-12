from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50, null=True, blank=True)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField('Температура при измерении')
    measurement_time = models.DateTimeField('Дата и время измерения', auto_now_add=True)
    image = models.ImageField('Снимок датчика', null=True, blank=True)