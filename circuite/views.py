from django.shortcuts import render, redirect
from django.conf import settings
import requests

from . import models
from . import forms


# prima pagina, aici arat toate circuitele sub forma de carduri
# daca cineva scrie ceva in bara de cautare, filtrez dupa nume
def pagina_principala(request):
    cautare = request.GET.get('cauta')
    if cautare:
        circuite = models.Circuit.objects.filter(nume__contains=cautare)
    else:
        circuite = models.Circuit.objects.all()

    date_pagina = {
        'circuite': circuite,
        'cautare': cautare,
    }
    return render(request, 'circuite/acasa.html', date_pagina)


# pagina cu detaliile unui circuit
# aici arat istoria, vremea de acum si comentariile lasate de lume
def detalii_circuit(request, id):
    circuit = models.Circuit.objects.get(id=id)
    marile_premii = models.MarePremiu.objects.filter(circuit=circuit)
    comentarii = models.Comentariu.objects.filter(circuit=circuit)

    # aici iau vremea de acum de la openweathermap
    # daca nu am cheie sau nu merge netul, las avem_vreme pe False
    # ca sa nu crape pagina si sa scriu ca vremea nu e disponibila
    avem_vreme = False
    vreme = {}
    cheie = settings.OPENWEATHER_API_KEY
    if cheie != '':
        adresa = 'https://api.openweathermap.org/data/2.5/weather'
        parametrii = {
            'lat': circuit.latitudine,
            'lon': circuit.longitudine,
            'appid': cheie,
            'units': 'metric',
            'lang': 'ro',
        }
        try:
            raspuns = requests.get(adresa, params=parametrii)
            if raspuns.status_code == 200:
                date_vreme = raspuns.json()
                vreme['temperatura'] = round(date_vreme['main']['temp'])
                vreme['descriere'] = date_vreme['weather'][0]['description']
                vreme['umiditate'] = date_vreme['main']['humidity']
                vreme['vant'] = date_vreme['wind']['speed']
                avem_vreme = True
        except:
            # daca ceva nu merge, ramanem fara vreme
            avem_vreme = False

    # formularul gol de comentariu ca sa apara pe pagina
    formular = forms.FormularComentariu()

    date_pagina = {
        'circuit': circuit,
        'marile_premii': marile_premii,
        'comentarii': comentarii,
        'avem_vreme': avem_vreme,
        'vreme': vreme,
        'formular': formular,
    }
    return render(request, 'circuite/detalii.html', date_pagina)


# aici primesc comentariul trimis de pe pagina de detalii
# il salvez si trimit omul inapoi la circuit
def adauga_comentariu(request, id):
    circuit = models.Circuit.objects.get(id=id)
    if request.method == 'POST':
        formular = forms.FormularComentariu(request.POST)
        if formular.is_valid():
            comentariu_nou = models.Comentariu()
            comentariu_nou.circuit = circuit
            comentariu_nou.nume_vizitator = formular.cleaned_data['nume_vizitator']
            comentariu_nou.mesaj = formular.cleaned_data['mesaj']
            comentariu_nou.save()
    return redirect('detalii', id=id)


# pagina cu formular unde pot adauga un circuit nou in baza de date
def adauga_circuit(request):
    if request.method == 'POST':
        formular = forms.FormularCircuit(request.POST)
        if formular.is_valid():
            formular.save()
            return redirect('acasa')
    else:
        formular = forms.FormularCircuit()

    date_pagina = {
        'formular': formular,
    }
    return render(request, 'circuite/adauga_circuit.html', date_pagina)


# pagina cu toate cursele din 2026, le pun in ordine dupa runda
def lista_curse(request):
    curse = models.MarePremiu.objects.order_by('runda')
    date_pagina = {
        'curse': curse,
    }
    return render(request, 'circuite/curse.html', date_pagina)
