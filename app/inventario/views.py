from django.shortcuts import render
from .models import ProveedorMateriaPrima

def lista_proveedores_materias(request):
    relaciones = ProveedorMateriaPrima.objects.select_related('proveedor', 'materia_prima')
    return render(request, 'inventario/lista_proveedores_materias.html', {'relaciones': relaciones})

