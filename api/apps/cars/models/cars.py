from django.db import models


class Brand(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, db_column='nombre')

    class Meta:
        db_table = 'marcas'


class Model(models.Model):

    id = models.AutoField(primary_key=True)
    brand = models.ForeignKey(
        'Brand',
        related_name='brand',
        db_column='marca',
        on_delete=models.DO_NOTHING,
    )
    name = models.CharField(max_length=255, db_column='nombre')

    class Meta:
        db_table = 'modelos'

class Car(models.Model):

    id = models.AutoField(primary_key=True)
    model = models.ForeignKey(
        'Model',
        related_name='model',
        db_column='modelo',
        on_delete=models.DO_NOTHING,
    )
    doors = models.IntegerField(db_column='puertas')
    high = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        db_column='alto',
    )
    long = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        db_column='largo',
    )
    width = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        db_column='ancho',
    )
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        db_column='peso',
    )
    diesel = models.BooleanField(null=False)
    description = models.TextField(null=True, db_column='descripcion')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'autos'


class CarAvailability(models.Model):

    id = models.AutoField(primary_key=True)
    car = models.ForeignKey(
        'Car',
        related_name='car',
        db_column='auto',
        on_delete=models.CASCADE,
    )
    available = models.BooleanField(default=True, db_column='disponible')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'disponibilidad_auto'
