from django.contrib import admin
from .models import Producto
from .models import Producto_bandanas
from .models import Producto_collares
from .models import Producto_identificadores
from .models import Producto_ofertas
from .models import Canasta
from .models import Pedido
# Register your models here.
admin.site.register(Producto)
admin.site.register(Producto_bandanas)
admin.site.register(Producto_collares)
admin.site.register(Producto_identificadores)
admin.site.register(Producto_ofertas)
admin.site.register(Canasta)
admin.site.register(Pedido)