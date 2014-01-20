from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.IntegerField()
    img = models.CharField(max_length=150)
    class Meta:
        db_table = u'producto'


