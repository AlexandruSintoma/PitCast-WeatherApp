from django import forms
from . import models


# formularul prin care adaug un circuit nou de pe site
# folosesc ModelForm ca sa nu mai scriu toate campurile de mana
class FormularCircuit(forms.ModelForm):
    class Meta:
        model = models.Circuit
        fields = [
            'nume',
            'tara',
            'oras',
            'latitudine',
            'longitudine',
            'lungime_km',
            'numar_viraje',
            'an_prima_cursa',
            'istorie',
            'imagine_url',
        ]


# formularul de comentariu de pe pagina unui circuit
# aici cer doar numele si mesajul, circuitul il pun eu in view
class FormularComentariu(forms.ModelForm):
    class Meta:
        model = models.Comentariu
        fields = ['nume_vizitator', 'mesaj']
