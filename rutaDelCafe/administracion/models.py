from django.db import models
#from django.contrib.auth.models import AbstractUser
# Create your models here.

# Usaremos el diagrama de clases


class Servicios(models.Model):

    TIPOS_SERVICIO_CHOICES = [
        ('ventaProductos', 'Venta de productos'),
        ('servicioRestaurante', 'Alojamiento'),
        ('produccionProductos', 'Produccion de productos'),
        ('atractivoTuristico', 'Atractivo Turistico'),
        ('hospedaje', 'Hospedaje'),
        ('cafeteria', 'Cafeteria'),
        ('piscina', 'Piscina'),
        ('camping', 'Camping'),
        ('caminata', 'Caminata'),
        ('cabalgata', 'Cabalgata'),
        ('recreacion', 'Recreacion'),
        ('comidaTipica', 'Comida Tipica'),
        ('comidaRapida', 'Comida Rapida'),
        ('comidaCoreana', 'Comida Coreana'),
    ]

    #nombreServicio = models.CharField(verbose_name="Nombre del Servicio", max_length=500)
    tipoServicio = models.CharField(verbose_name="Tipo de servicio", max_length=20, choices=TIPOS_SERVICIO_CHOICES, null=True, blank=True)
    precio = models.CharField(verbose_name="Precio", max_length=6, null=True, blank=True)
    descripcionServicio = models.CharField(
        verbose_name="Descripcion del Servicio", max_length=500)

class Multimedia(models.Model):
    descripcion = models.CharField(verbose_name="Descripcion", max_length=200, null=True, blank=True)
    imagen = models.ImageField(upload_to="Imagenes del emprendimiento", verbose_name="Subir imagenes del emprendimiento", blank=True, null=True)
    video = models.URLField(verbose_name="video promocional", blank=True, null=True)

class Productos(models.Model):
    nombre_producto = models.CharField(verbose_name="Nombre del producto", max_length=100, null=True, blank=True)
    precio = models.CharField(verbose_name="Precio del producto unitario", max_length=5, null=True, blank=True)
    descripcion = models.CharField(verbose_name="Descripcion del producto", max_length=200, null=True, blank=True)
    imagen = models.ImageField(upload_to="Imagenes del producto", verbose_name="Subir imagenes del producto", blank=True, null=True)


class Emprendimiento(models.Model):

    TIPOS_CALIFICACION_CHOICES = [
        ('bueno', 'Bueno'),
        ('malo', 'Malo'),
        ('regular', 'Regular'),
        ('normal', 'Normal'),
        ('excelentes', 'Excelente'),
    ]

    DISPONIBILIDAD_CHOICES = [
        ('si', 'Si'),
        ('no', 'No'),
    ]

    nombreEmprendiento = models.CharField(
        verbose_name="Nombre del Emprendimiento", max_length=500)
    direccionEmprendiento = models.CharField(
        verbose_name="Direccion", max_length=500)
    telCelular = models.CharField(
        verbose_name="Telefono celular", max_length=13)
    telFijo = models.CharField(verbose_name="Telefono Fijo", max_length=13)
    descripcion = models.TextField(verbose_name="Descripcion")
    horaApertura = models.DateTimeField()
    horaCierre = models.DateTimeField()
    latitud = models.CharField(verbose_name="Latitud", max_length=50)
    altitud = models.CharField(verbose_name="Altitud", max_length=50)
    #imagen = models.ImageField(upload_to="fotosEmprendimiento", otra clase
    multimedia = models.ManyToManyField(Multimedia)                  
    disponibilidad = models.CharField(
        verbose_name="Disponibilidad", max_length=3, choices=DISPONIBILIDAD_CHOICES, blank=True, null=True)
    calificacion = models.CharField(
        verbose_name="Calificacion", max_length=20, choices=TIPOS_CALIFICACION_CHOICES, blank=True, null=True)
    resena = models.CharField(verbose_name="Resena",
                              max_length=500, blank=True, null=True)
    servicios = models.ManyToManyField(Servicios)
    producto = models.ManyToManyField(Productos)

    def __str__(self):
        return self.nombreEmprendiento

    class Meta:
        verbose_name = "Emprendiento"
        verbose_name_plural = "Emprendientos"


class Persona(models.Model):

    TIPO_DOCUMENTO_CHOICE = [
        ('cedula', 'Cedula'),
        ('pasaporte', 'Pasaporte'),
    ]

    email = models.EmailField(max_length=150, unique=True, null=True)
    tipo_documento = models.CharField(verbose_name="Tipo de documento", max_length=20, choices=TIPO_DOCUMENTO_CHOICE, null=True, blank=True)
    cedula = models.CharField(verbose_name="Cedula", max_length=13)
    firstName = models.CharField(verbose_name="Nombres", max_length=200, null=True, blank=True)
    lastName = models.CharField(verbose_name="Apellidos", max_length=200, null=True, blank=True)
    telefono = models.CharField(verbose_name="Numero de telefono", max_length=13)
    direccion = models.CharField(verbose_name="Direccion", max_length=500)
    fechaNacmiento = models.DateField(verbose_name="Fecha de Nacmiento")
    nacionalidad = models.CharField(verbose_name="Nacionalidad", max_length=50)
    foto = models.ImageField(upload_to="fotosUsuarios",
                             verbose_name="Subir su foto de usuario", blank=True, null=True)

    # metodo para presentar el objeto creado

    def __str__(self):
        return self.cedula

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"


class Cliente(Persona):

    paisOrigen = models.CharField(
        verbose_name="Pais de origen", max_length=200)


class Administrador(Persona):

    fechaInicio = models.DateTimeField(verbose_name="Fecha de inicio")
    fechaActualizacion = models.DateTimeField(
        verbose_name="Fecha de actualizacion")
    estado = models.BooleanField()

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"


class Emprendedor(Persona):

    # relacion de 1 a muchos
    emprendimientos = models.ManyToManyField(Emprendimiento, blank=True)

    class Meta:
        verbose_name = "Emprendedor"
        verbose_name_plural = "Emprendedores"


class Reservas(models.Model):
    fechaLlegada = models.DateField(verbose_name="Ingrese la fecha de llegada")
    fechaSalida = models.DateField(verbose_name="Ingrese la fecha de salida")
    numPersonas = models.IntegerField(
        verbose_name="Ingrese el numero de personas")
    descripcion = models.CharField(
        verbose_name="Alguna descripcion al momento de la reserva", max_length=500)
    # add tipo de productos a comprar para reservarlos
    productos = models.ManyToManyField(Productos)
