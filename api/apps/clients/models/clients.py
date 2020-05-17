from django.db import models


class Client(models.Model):

    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        db_column='nombre',
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        db_column='apellido',
    )
    status = models.BooleanField(
        default=True,
        db_column='client_disponible',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'clientes'

