from django.db import models

from apps.clients.models import Client
from . import Car


class CarHistory(models.Model):

    REQUESTED = 'solicitado'
    IN_USE = 'en uso'
    RETURNED = 'devuelto'

    STATUS_CHOICE = (
        (REQUESTED, REQUESTED),
        (IN_USE, IN_USE),
        (RETURNED, RETURNED),
    )

    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(
        'Client',
        related_name='client',
        db_column='cliente'
        on_delete=models.DO_NOTHING,
    )
    car = models.ForeignKey(
        'Car',
        related_name='car',
        db_column='auto'
        on_delete=models.DO_NOTHING,
    )
    status = models.CharField(
        choices=STATUS_CHOICE,
        null=False,
        db_column='estado',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'historial_autos'


class CarIncidents(models.Model):

    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(
        'Client',
        related_name='client',
        db_column='cliente'
        on_delete=models.DO_NOTHING,
    )
    car = models.ForeignKey(
        'Car',
        related_name='car',
        db_column='auto'
        on_delete=models.DO_NOTHING,
    )
    description = models.TextField(null=False)

    class Meta:
        db_table = 'incidencias'
