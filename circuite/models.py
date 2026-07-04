from django.db import models


# aici tin toate circuitele de formula 1 din 2026
# fiecare circuit are date despre el si o mica istorie
class Circuit(models.Model):
    nume = models.CharField(max_length=200)
    tara = models.CharField(max_length=100)
    oras = models.CharField(max_length=100)
    latitudine = models.FloatField()
    longitudine = models.FloatField()
    lungime_km = models.FloatField()
    numar_viraje = models.IntegerField()
    an_prima_cursa = models.IntegerField()
    istorie = models.TextField()
    imagine_url = models.CharField(max_length=500)
    data_adaugarii = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'circuit'

    # ca sa apara numele frumos in admin, nu Circuit object(1)
    def __str__(self):
        return self.nume


# marile premii din 2026, fiecare e legat de un circuit
# aici folosesc foreign key ca sa leg cursa de circuitul ei
class MarePremiu(models.Model):
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    nume = models.CharField(max_length=200)
    runda = models.IntegerField()
    data_cursei = models.DateField()

    class Meta:
        db_table = 'mare_premiu'

    def __str__(self):
        return self.nume


# aici salvez parerile lasate de vizitatori pe pagina unui circuit
# si asta e legat de circuit tot prin foreign key
class Comentariu(models.Model):
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    nume_vizitator = models.CharField(max_length=100)
    mesaj = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comentariu'

    def __str__(self):
        return self.nume_vizitator
