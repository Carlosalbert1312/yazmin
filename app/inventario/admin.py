from django.contrib import admin
from .models import Pastel, Receta, MateriaPrima, Proveedor, ProveedorMateriaPrima

# ---------- Inlines ----------
class RecetaInline(admin.TabularInline):
    model = Receta
    extra = 1  # Muestra una línea vacía por default
    autocomplete_fields = ['materia_prima']  # si quieres buscador

class ProveedorMateriaPrimaInline(admin.TabularInline):
    model = ProveedorMateriaPrima
    extra = 1
    autocomplete_fields = ['materia_prima']

# ---------- Admins ----------
@admin.register(Pastel)
class PastelAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    inlines = [RecetaInline]

@admin.register(MateriaPrima)
class MateriaPrimaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'cantidad', 'unidad')
    search_fields = ('nombre', 'marca')

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono')
    search_fields = ('nombre',)
    inlines = [ProveedorMateriaPrimaInline]

@admin.register(ProveedorMateriaPrima)
class ProveedorMateriaPrimaAdmin(admin.ModelAdmin):
    list_display = ('proveedor', 'materia_prima', 'precio_unitario', 'fecha_actualizacion')
    list_filter = ('proveedor', 'materia_prima')

