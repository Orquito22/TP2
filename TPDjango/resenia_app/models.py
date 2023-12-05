from django.db import models

# Create your models here.

class Resenia(models.Model):
    """
    Atributos de clase que son usadas por herencia de la clase Model

    """
    ESTRELLAS = [
        ("⭐", "1 ESTRELLA"),
        ("⭐⭐", "2 ESTRELLAS"),
        ("⭐⭐⭐", "3 ESTRELLAS"),
        ("⭐⭐⭐⭐", "4 ESTRELLAS"),
        ("⭐⭐⭐⭐⭐", "5 ESTRELLAS"),
    ]

    nombre  =  models.CharField(max_length=200)
    empresa =  models.CharField(max_length=200)
    calificacion = models.CharField(max_length=5, choices=ESTRELLAS)
    resenia = models.CharField(max_length=200)
    fecha = models.DateField(auto_now=True)

  
    class Meta:
        db_table = "Reseña de clientes"


    def __str__(self):
        return f"La empresa: {self.nombre}, el dia {self.fecha} dejó una calificacion de {self.calificacion} y dijo: {self.resenia}"
        

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]
