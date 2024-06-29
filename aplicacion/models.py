from django.db import models

# Create your models here.

class Producto(models.Model):
    imagen = models.ImageField(upload_to='productos/')
    nombre = models.CharField(max_length=100)
    texto = models.CharField(max_length=100)
    precio = models.CharField(max_length=50)
    
    def _str_(self):
        return self.nombre
    

class Producto_bandanas(models.Model):
    imagen = models.ImageField(upload_to='productos/')
    nombre = models.CharField(max_length=100)
    texto = models.CharField(max_length=100)
    precio = models.CharField(max_length=50)
    
    def _str_(self):
        return self.nombre
    
class Producto_collares(models.Model):
    imagen = models.ImageField(upload_to='productos/')
    nombre = models.CharField(max_length=100)
    texto = models.CharField(max_length=100)
    precio = models.CharField(max_length=50)
    
    def _str_(self):
        return self.nombre
    
class Producto_identificadores(models.Model):
    imagen = models.ImageField(upload_to='productos/')
    nombre = models.CharField(max_length=100)
    texto = models.CharField(max_length=100)
    precio = models.CharField(max_length=50)
    
    def _str_(self):
        return self.nombre
    
class Producto_ofertas(models.Model):
    imagen = models.ImageField(upload_to='productos/')
    nombre = models.CharField(max_length=100)
    texto = models.CharField(max_length=100)
    precio = models.CharField(max_length=50)
    
    def _str_(self):
        return self.nombre
    
#Tabla para productos en el canasto   
class Canasta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True )
    cantidad = models.PositiveIntegerField(default=1)
    bandanas = models.ForeignKey(Producto_bandanas, on_delete=models.CASCADE, null=True, blank=True)
    collares = models.ForeignKey(Producto_collares, on_delete=models.CASCADE, null=True, blank=True)
    identificadores = models.ForeignKey(Producto_identificadores, on_delete=models.CASCADE, null=True, blank=True)
    ofertas = models.ForeignKey(Producto_ofertas, on_delete=models.CASCADE, null=True, blank=True)

    def _str_(self):
        return f'{self.cantidad} x {self.producto.nombre}'
    
    def get_product_name(self):
        if self.producto:
            return self.producto.nombre
        elif self.bandanas:
            return self.bandanas.nombre
        elif self.collares:
            return self.collares.nombre
        elif self.identificadores:
            return self.identificadores.nombre
        elif self.ofertas:
            return self.ofertas.nombre
        return 'Sin producto'























