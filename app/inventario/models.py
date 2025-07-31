from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    direccion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class MateriaPrima(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    unidad = models.CharField(max_length=20, choices=[
        ('g', 'Gramos'),
        ('ml', 'Mililitros'),
        ('pz', 'Piezas'),
        ]) 
    def __str__(self):
        return self.nombre

class ProveedorMateriaPrima(models.Model):
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
    materia_prima = models.ForeignKey('MateriaPrima', on_delete=models.CASCADE)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_actualizacion = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.proveedor.nombre} - {self.materia_prima.nombre}"

class Pastel(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Receta(models.Model):
    pastel = models.ForeignKey(Pastel, on_delete=models.CASCADE, related_name='ingredientes')
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} de {self.materia_prima.nombre} para {self.pastel.nombre}"


