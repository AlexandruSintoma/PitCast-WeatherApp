# scriptul asta il rulez o singura data ca sa pun circuitele in baza de date
# ca sa nu le adaug pe toate de mana din admin
# il pornesc cu: python incarca_date.py

import os
import django
from datetime import date

# ii spun lui django unde sunt setarile ca sa pot folosi baza de date
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pitcast.settings')
django.setup()

from circuite import models

# sterg ce era inainte ca sa nu am circuite duble daca rulez de mai multe ori
models.Circuit.objects.all().delete()


# Bahrain
circuit1 = models.Circuit.objects.create(
    nume='Bahrain International Circuit',
    tara='Bahrain',
    oras='Sakhir',
    latitudine=26.0325,
    longitudine=50.5106,
    lungime_km=5.412,
    numar_viraje=15,
    an_prima_cursa=2004,
    istorie='Construit in mijlocul desertului, este locul unde de multe ori incepe sezonul. Se alearga si seara, sub lumini, iar nisipul de langa pista face totul mai spectaculos.',
    imagine_url='https://placehold.co/600x340/15151e/e10600/png?text=Bahrain',
)
models.MarePremiu.objects.create(
    circuit=circuit1,
    nume='Marele Premiu al Bahrainului',
    runda=1,
    data_cursei=date(2026, 3, 8),
)

# Arabia Saudita
circuit2 = models.Circuit.objects.create(
    nume='Jeddah Corniche Circuit',
    tara='Arabia Saudita',
    oras='Jeddah',
    latitudine=21.6319,
    longitudine=39.1044,
    lungime_km=6.174,
    numar_viraje=27,
    an_prima_cursa=2021,
    istorie='Este cel mai rapid circuit de strada din calendar. Trece pe langa malul marii si are foarte multe viraje rapide, unde nu prea ai loc de greseli.',
    imagine_url='https://placehold.co/600x340/15151e/e10600/png?text=Jeddah',
)
models.MarePremiu.objects.create(
    circuit=circuit2,
    nume='Marele Premiu al Arabiei Saudite',
    runda=2,
    data_cursei=date(2026, 3, 15),
)

# Australia
circuit3 = models.Circuit.objects.create(
    nume='Albert Park Circuit',
    tara='Australia',
    oras='Melbourne',
    latitudine=-37.8497,
    longitudine=144.968,
    lungime_km=5.278,
    numar_viraje=14,
    an_prima_cursa=1996,
    istorie='Este un circuit facut in jurul unui lac dintr-un parc din Melbourne. Doar in weekendul cursei se transforma in pista de formula 1, in rest e drum normal.',
    imagine_url='https://placehold.co/600x340/15151e/e10600/png?text=Melbourne',
)
models.MarePremiu.objects.create(
    circuit=circuit3,
    nume='Marele Premiu al Australiei',
    runda=3,
    data_cursei=date(2026, 3, 29),
)

# Japonia
circuit4 = models.Circuit.objects.create(
    nume='Suzuka International Racing Course',
    tara='Japonia',
    oras='Suzuka',
    latitudine=34.8431,
    longitudine=136.541,
    lungime_km=5.807,
    numar_viraje=18,
    an_prima_cursa=1987,
    istorie='Este iubit de aproape toti pilotii pentru ca e greu si tehnic. Are forma de opt, adica pista trece pe deasupra ei insasi, ceva rar la circuitele de formula 1.',
    imagine_url='https://placehold.co/600x340/15151e/e10600/png?text=Suzuka',
)
models.MarePremiu.objects.create(
    circuit=circuit4,
    nume='Marele Premiu al Japoniei',
    runda=4,
    data_cursei=date(2026, 4, 12),
)

# Statele Unite - Miami
circuit5 = models.Circuit.objects.create(
    nume='Miami International Autodrome',
    tara='Statele Unite',
    oras='Miami',
    latitudine=25.9581,
    longitudine=-80.2389,
    lungime_km=5.412,
    numar_viraje=19,
    an_prima_cursa=2022,
    istorie='Este construit in jurul stadionului echipei de fotbal american Miami Dolphins. E un circuit nou, cu multa atmosfera si multe vedete in tribune.',
    imagine_url='https://placehold.co/600x340/15151e/e10600/png?text=Miami',
)
models.MarePremiu.objects.create(
    circuit=circuit5,
    nume='Marele Premiu al orasului Miami',
    runda=5,
    data_cursei=date(2026, 5, 3),
)

# Monaco
circuit6 = models.Circuit.objects.create(
    nume='Circuit de Monaco',
    tara='Monaco',
    oras='Monte Carlo',
    latitudine=43.7347,
    longitudine=7.4206,
    lungime_km=3.337,
    numar_viraje=19,
    an_prima_cursa=1950,
    istorie='Este cea mai celebra cursa din tot sezonul. Se merge pe strazile inguste din Monte Carlo, printre cladiri si langa port. Depasirile sunt aproape imposibile aici.',
    imagine_url='https://placehold.co/600x340/15151e/e10600/png?text=Monaco',
)
models.MarePremiu.objects.create(
    circuit=circuit6,
    nume='Marele Premiu de la Monaco',
    runda=6,
    data_cursei=date(2026, 5, 24),
)

# Spania
circuit7 = models.Circuit.objects.create(
    nume='Circuit de Barcelona-Catalunya',
    tara='Spania',
    oras='Barcelona',
    latitudine=41.57,
    longitudine=2.2611,
    lungime_km=4.657,
    numar_viraje=16,
    an_prima_cursa=1991,
    istorie='Este circuitul pe care echipele il cunosc cel mai bine, pentru ca aici se fac multe teste inainte de sezon. Are de toate: viraje rapide, viraje lente si o linie dreapta lunga.',
    imagine_url='https://placehold.co/600x340/15151e/e10600/png?text=Barcelona',
)
models.MarePremiu.objects.create(
    circuit=circuit7,
    nume='Marele Premiu al Spaniei',
    runda=7,
    data_cursei=date(2026, 6, 7),
)

# Canada
circuit8 = models.Circuit.objects.create(
    nume='Circuit Gilles Villeneuve',
    tara='Canada',
    oras='Montreal',
    latitudine=45.5,
    longitudine=-73.5228,
    lungime_km=4.361,
    numar_viraje=14,
    an_prima_cursa=1978,
    istorie='Este pe o insula artificiala din Montreal si poarta numele unui pilot canadian iubit. Are un zid faimos numit Zidul Campionilor, in care au intrat multi piloti mari.',
    imagine_url='https://placehold.co/600x340/15151e/e10600/png?text=Montreal',
)
models.MarePremiu.objects.create(
    circuit=circuit8,
    nume='Marele Premiu al Canadei',
    runda=8,
    data_cursei=date(2026, 6, 14),
)

# Marea Britanie
circuit9 = models.Circuit.objects.create(
    nume='Silverstone Circuit',
    tara='Marea Britanie',
    oras='Silverstone',
    latitudine=52.0733,
    longitudine=-1.0142,
    lungime_km=5.891,
    numar_viraje=18,
    an_prima_cursa=1950,
    istorie='Aici s-a alergat prima cursa din istoria campionatului mondial de formula 1, in 1950. E construit pe un fost aerodrom si are viraje foarte rapide.',
    imagine_url='https://placehold.co/600x340/15151e/e10600/png?text=Silverstone',
)
models.MarePremiu.objects.create(
    circuit=circuit9,
    nume='Marele Premiu al Marii Britanii',
    runda=9,
    data_cursei=date(2026, 7, 5),
)

# Belgia
circuit10 = models.Circuit.objects.create(
    nume='Circuit de Spa-Francorchamps',
    tara='Belgia',
    oras='Spa',
    latitudine=50.4372,
    longitudine=5.9714,
    lungime_km=7.004,
    numar_viraje=19,
    an_prima_cursa=1950,
    istorie='Este cel mai lung circuit din calendar si e asezat printre dealuri si paduri. Are virajul Eau Rouge, unul dintre cele mai tari viraje din toata lumea. Aici ploua des.',
    imagine_url='https://placehold.co/600x340/15151e/e10600/png?text=Spa',
)
models.MarePremiu.objects.create(
    circuit=circuit10,
    nume='Marele Premiu al Belgiei',
    runda=10,
    data_cursei=date(2026, 7, 26),
)

# Italia
circuit11 = models.Circuit.objects.create(
    nume='Autodromo Nazionale Monza',
    tara='Italia',
    oras='Monza',
    latitudine=45.6156,
    longitudine=9.2811,
    lungime_km=5.793,
    numar_viraje=11,
    an_prima_cursa=1950,
    istorie='Este numit Templul Vitezei pentru ca aici se ating cele mai mari viteze din sezon. Fanii echipei Ferrari, numiti tifosi, umplu tribunele in fiecare an.',
    imagine_url='https://placehold.co/600x340/15151e/e10600/png?text=Monza',
)
models.MarePremiu.objects.create(
    circuit=circuit11,
    nume='Marele Premiu al Italiei',
    runda=11,
    data_cursei=date(2026, 9, 6),
)

# Singapore
circuit12 = models.Circuit.objects.create(
    nume='Marina Bay Street Circuit',
    tara='Singapore',
    oras='Singapore',
    latitudine=1.2914,
    longitudine=103.864,
    lungime_km=4.94,
    numar_viraje=19,
    an_prima_cursa=2008,
    istorie='A fost prima cursa de formula 1 care s-a alergat noaptea, sub lumini. Se merge pe strazile orasului, iar caldura si umezeala fac cursa foarte grea pentru piloti.',
    imagine_url='https://placehold.co/600x340/15151e/e10600/png?text=Singapore',
)
models.MarePremiu.objects.create(
    circuit=circuit12,
    nume='Marele Premiu de la Singapore',
    runda=12,
    data_cursei=date(2026, 9, 20),
)


print('Gata! Am adaugat toate circuitele in baza de date.')
