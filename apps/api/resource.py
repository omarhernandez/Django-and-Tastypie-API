from django.db.models import Q
from tastypie import fields
from apps.producto.models import *
from tastypie.exceptions import BadRequest
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource , ALL , ALL_WITH_RELATIONS

class ProductoResource(ModelResource):

	"""
	Producto - Informacion 	, nombre , imagen , costo , ID del producto
	"""

	nombre = fields.CharField(attribute='nombre')
	descripcion = fields.CharField(attribute='descripcion')

	class Meta:
		allowed_methods = ['get', 'post' , 'delete']		
		queryset = Producto.objects.all().distinct()
		resource_name = 'producto'
		authorization= Authorization()

		filtering = {
			"nombre" : ["icontains"],
			"descripcion" : ["icontains"],
		}



