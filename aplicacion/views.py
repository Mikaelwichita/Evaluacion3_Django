from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .models import Producto_bandanas
from .models import Producto_collares
from .models import Producto_identificadores
from .models import Producto_ofertas
from .models import Canasta
from .forms import ProductoForms
from .forms import Producto_bandanasForms
from .forms import Producto_collaresForms
from .forms import Producto_identificadoresForms
from .forms import Producto_ofertasForms
# Create your views here.



def index(request):
    productos = Producto.objects.all()
    return render(request, 'paginas/index.html', {'productos': productos})

def bandanas(request):
    productos = Producto_bandanas.objects.all()
    return render(request, 'paginas/bandanas.html', {'productos': productos})

def collares(request):
    productos = Producto_collares.objects.all()
    return render(request, 'paginas/collares.html', {'productos': productos})

def identificadores(request):
    productos = Producto_identificadores.objects.all()
    return render(request, 'paginas/identificadores.html', {'productos': productos})

def ofertas(request):
    productos = Producto_ofertas.objects.all()
    return render(request, 'paginas/ofertas.html', {'productos': productos})

def ayuda(request):
    context={}
    return render(request,'paginas/ayuda.html',context)

def ver_canasta(request):
    canasta_items = Canasta.objects.all()
    
    def clean_price(price_str):
        # Elimina el signo de dólar y el separador de miles.
        price_str = price_str.replace('$', '').replace('.', '').replace(',', '.')
        return int(price_str)

    total = 0
    for item in canasta_items:
        if item.producto and item.producto.precio:
            total += clean_price(item.producto.precio) * item.cantidad
        elif item.bandanas and item.bandanas.precio:
            total += clean_price(item.bandanas.precio) * item.cantidad
        elif item.collares and item.collares.precio:
            total += clean_price(item.collares.precio) * item.cantidad
        elif item.identificadores and item.identificadores.precio:
            total += clean_price(item.identificadores.precio) * item.cantidad
        elif item.ofertas and item.ofertas.precio:
            total += clean_price(item.ofertas.precio) * item.cantidad

    return render(request, 'paginas/canasta.html', {'canasta_items': canasta_items, 'total': total})

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    item, created = Canasta.objects.get_or_create(producto=producto)
    if not created:
        item.cantidad += 1
        item.save()
    return redirect('ver_canasta')


def agregar_al_carrito_bandana(request, producto_id):
    producto = get_object_or_404(Producto_bandanas, id=producto_id)
    item, created = Canasta.objects.get_or_create(bandanas=producto)
    if not created:
        item.cantidad += 1
        item.save()
    return redirect('ver_canasta')


def agregar_al_carrito_collares(request, producto_id):
    producto = get_object_or_404(Producto_collares, id=producto_id)
    item, created = Canasta.objects.get_or_create(collares=producto)
    if not created:
        item.cantidad += 1
        item.save()
    return redirect('ver_canasta')

def agregar_al_carrito_identificadores(request, producto_id):
    producto = get_object_or_404(Producto_identificadores, id=producto_id)
    item, created = Canasta.objects.get_or_create(identificadores=producto)
    if not created:
        item.cantidad += 1
        item.save()
    return redirect('ver_canasta')

def agregar_al_carrito_ofertas(request, producto_id):
    producto = get_object_or_404(Producto_ofertas, id=producto_id)
    item, created = Canasta.objects.get_or_create(ofertas=producto)
    if not created:
        item.cantidad += 1
        item.save()
    return redirect('ver_canasta')


def eliminar_del_carrito(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Canasta, id=item_id)
        item.delete()
        return redirect('ver_canasta')
    

def fundacion(request):
    context={}
    return render(request,'paginas/fundacion.html',context)

def registro(request):
    context={}
    return render(request,'paginas/registro.html',context)

def micuenta(request):
    context={}
    return render(request,'paginas/micuenta.html',context)

################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################
################################################################################################################################

############ funcion de listado productos

def lista_productos(request):
    productos_index = Producto.objects.all()
    productos_bandanas = Producto_bandanas.objects.all()
    productos_collares = Producto_collares.objects.all()
    productos_identificadores = Producto_identificadores.objects.all()
    productos_ofertas = Producto_ofertas.objects.all()

    return render(request, 'paginas/admin_listado.html', {
        'productos_index': productos_index,
        'productos_bandanas': productos_bandanas,
        'productos_collares': productos_collares,
        'productos_identificadores': productos_identificadores,
        'productos_ofertas': productos_ofertas,
    })


###### FUNCIONES PARA AGREGAR PRODUCTOS


# Vista para agregar un producto en index 

def agregar_producto_index(request):
    if request.method == 'POST':
        form = ProductoForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForms()
    return render(request, 'paginas/admin_agregar_index.html', {'form': form})

# Vista para agregar un producto en bandanas 


def agregar_producto_bandanas(request):
    if request.method == 'POST':
        form = Producto_bandanasForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = Producto_bandanasForms()
    return render(request, 'paginas/admin_agregar_bandanas.html', {'form': form})

# Vista para agregar un producto en collares


def agregar_producto_collares(request):
    if request.method == 'POST':
        form = Producto_collaresForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = Producto_collaresForms()
    return render(request, 'paginas/admin_agregar_collares.html', {'form': form})

# Vista para agregar un producto en identificadores


def agregar_producto_identificadores(request):
    if request.method == 'POST':
        form = Producto_identificadoresForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = Producto_identificadoresForms()
    return render(request, 'paginas/admin_agregar_identificadores.html', {'form': form})

# Vista para agregar un producto en ofertas

def agregar_producto_ofertas(request):
    if request.method == 'POST':
        form = Producto_ofertasForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = Producto_ofertasForms()
    return render(request, 'paginas/admin_agregar_ofertas.html', {'form': form})


###### FUNCIONES PARA ELIMINAR PRODUCTOS


#vista para eliminar los productos de index

def eliminar_producto_index(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'paginas/admin_eliminar_index.html', {'producto': producto})

#vista para eliminar los productos de bandanas

def eliminar_producto_bandanas(request, producto_id):
    producto = get_object_or_404(Producto_bandanas, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'paginas/admin_eliminar_bandanas.html', {'producto': producto})

#vista para eliminar los productos de collares

def eliminar_producto_collares(request, producto_id):
    producto = get_object_or_404(Producto_collares, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'paginas/admin_eliminar_collares.html', {'producto': producto})

#vista para eliminar los productos de identificadores

def eliminar_producto_identificadores(request, producto_id):
    producto = get_object_or_404(Producto_identificadores, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'paginas/admin_eliminar_identificadores.html', {'producto': producto})


#vista para eliminar los productos de ofertas

def eliminar_producto_ofertas(request, producto_id):
    producto = get_object_or_404(Producto_ofertas, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'paginas/admin_eliminar_ofertas.html', {'producto': producto})

###### FUNCIONES PARA MODIFICAR PRODUCTOS

#vista para editar los productos desde el admin

def modificar_producto_index(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForms(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForms(instance=producto)
    return render(request, 'paginas/admin_modificar_index.html', {'form': form, 'producto': producto})



def modificar_producto_bandanas(request, producto_id):
    producto = get_object_or_404(Producto_bandanas, id=producto_id)
    if request.method == 'POST':
        form = Producto_bandanasForms(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = Producto_bandanasForms(instance=producto)
    return render(request, 'paginas/admin_modificar_bandanas.html', {'form': form, 'producto': producto})


def modificar_producto_collares(request, producto_id):
    producto = get_object_or_404(Producto_collares, id=producto_id)
    if request.method == 'POST':
        form = Producto_collaresForms(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = Producto_collaresForms(instance=producto)
    return render(request, 'paginas/admin_modificar_collares.html', {'form': form, 'producto': producto})


def modificar_producto_collares(request, producto_id):
    producto = get_object_or_404(Producto_identificadores, id=producto_id)
    if request.method == 'POST':
        form = Producto_identificadoresForms(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = Producto_identificadoresForms(instance=producto)
    return render(request, 'paginas/admin_modificar_identificadores.html', {'form': form, 'producto': producto})

def modificar_producto_ofertas(request, producto_id):
    producto = get_object_or_404(Producto_ofertas, id=producto_id)
    if request.method == 'POST':
        form = Producto_ofertasForms(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = Producto_ofertasForms(instance=producto)
    return render(request, 'paginas/admin_modificar_ofertas.html', {'form': form, 'producto': producto})
