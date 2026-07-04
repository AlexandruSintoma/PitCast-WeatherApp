# scriptul asta il rulez o singura data ca sa pun circuitele in baza de date
# ca sa nu le adaug pe toate de mana din admin
# sunt toate cele 22 de curse din calendarul de formula 1 din 2026, in ordine
# (Bahrain si Arabia Saudita au fost anulate, asa au ramas 22 in loc de 24)
# la imagine_url pun calea catre poza din folderul static
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


# Runda 1 - Australia
circuit1 = models.Circuit.objects.create(
    nume='Albert Park Circuit',
    tara='Australia',
    oras='Melbourne',
    latitudine=-37.8497,
    longitudine=144.968,
    lungime_km=5.278,
    numar_viraje=14,
    an_prima_cursa=1996,
    istorie='Este un circuit facut in jurul unui lac dintr-un parc din Melbourne. Doar in weekendul cursei se transforma in pista de formula 1, in rest e drum normal.',
    imagine_url='circuite/img/Melbourne.png',
)
models.MarePremiu.objects.create(
    circuit=circuit1,
    nume='Marele Premiu al Australiei',
    runda=1,
    data_cursei=date(2026, 3, 8),
)

# Runda 2 - China
circuit2 = models.Circuit.objects.create(
    nume='Shanghai International Circuit',
    tara='China',
    oras='Shanghai',
    latitudine=31.3389,
    longitudine=121.22,
    lungime_km=5.451,
    numar_viraje=16,
    an_prima_cursa=2004,
    istorie='Are un viraj lung in forma de melc chiar la inceput, care se strange tot mai mult. Prima cursa aici a fost in 2004 si are o linie dreapta foarte lunga.',
    imagine_url='circuite/img/Shanghai.png',
)
models.MarePremiu.objects.create(
    circuit=circuit2,
    nume='Marele Premiu al Chinei',
    runda=2,
    data_cursei=date(2026, 3, 15),
)

# Runda 3 - Japonia
circuit3 = models.Circuit.objects.create(
    nume='Suzuka International Racing Course',
    tara='Japonia',
    oras='Suzuka',
    latitudine=34.8431,
    longitudine=136.541,
    lungime_km=5.807,
    numar_viraje=18,
    an_prima_cursa=1987,
    istorie='Este iubit de aproape toti pilotii pentru ca e greu si tehnic. Are forma de opt, adica pista trece pe deasupra ei insasi, ceva rar la circuitele de formula 1.',
    imagine_url='circuite/img/Suzuka.png',
)
models.MarePremiu.objects.create(
    circuit=circuit3,
    nume='Marele Premiu al Japoniei',
    runda=3,
    data_cursei=date(2026, 3, 29),
)

# Runda 4 - Statele Unite (Miami)
circuit4 = models.Circuit.objects.create(
    nume='Miami International Autodrome',
    tara='Statele Unite',
    oras='Miami',
    latitudine=25.9581,
    longitudine=-80.2389,
    lungime_km=5.412,
    numar_viraje=19,
    an_prima_cursa=2022,
    istorie='Este construit in jurul stadionului echipei de fotbal american Miami Dolphins. E un circuit nou, cu multa atmosfera si multe vedete in tribune.',
    imagine_url='circuite/img/Miami.png',
)
models.MarePremiu.objects.create(
    circuit=circuit4,
    nume='Marele Premiu al orasului Miami',
    runda=4,
    data_cursei=date(2026, 5, 3),
)

# Runda 5 - Canada
circuit5 = models.Circuit.objects.create(
    nume='Circuit Gilles Villeneuve',
    tara='Canada',
    oras='Montreal',
    latitudine=45.5,
    longitudine=-73.5228,
    lungime_km=4.361,
    numar_viraje=14,
    an_prima_cursa=1978,
    istorie='Este pe o insula artificiala din Montreal si poarta numele unui pilot canadian iubit. Are un zid faimos numit Zidul Campionilor, in care au intrat multi piloti mari.',
    imagine_url='circuite/img/Montreal.png',
)
models.MarePremiu.objects.create(
    circuit=circuit5,
    nume='Marele Premiu al Canadei',
    runda=5,
    data_cursei=date(2026, 5, 24),
)

# Runda 6 - Monaco
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
    imagine_url='circuite/img/Monaco.png',
)
models.MarePremiu.objects.create(
    circuit=circuit6,
    nume='Marele Premiu de la Monaco',
    runda=6,
    data_cursei=date(2026, 6, 7),
)

# Runda 7 - Spania (Barcelona)
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
    imagine_url='circuite/img/Barcelona.png',
)
models.MarePremiu.objects.create(
    circuit=circuit7,
    nume='Marele Premiu de la Barcelona',
    runda=7,
    data_cursei=date(2026, 6, 14),
)

# Runda 8 - Austria
circuit8 = models.Circuit.objects.create(
    nume='Red Bull Ring',
    tara='Austria',
    oras='Spielberg',
    latitudine=47.2197,
    longitudine=14.7647,
    lungime_km=4.318,
    numar_viraje=10,
    an_prima_cursa=1970,
    istorie='Este un circuit scurt, asezat printre dealurile din Austria. Se termina repede un tur, asa ca masinile trec des unele pe langa altele.',
    imagine_url='circuite/img/Spielberg.png',
)
models.MarePremiu.objects.create(
    circuit=circuit8,
    nume='Marele Premiu al Austriei',
    runda=8,
    data_cursei=date(2026, 6, 28),
)

# Runda 9 - Marea Britanie
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
    imagine_url='circuite/img/Silverstone.png',
)
models.MarePremiu.objects.create(
    circuit=circuit9,
    nume='Marele Premiu al Marii Britanii',
    runda=9,
    data_cursei=date(2026, 7, 5),
)

# Runda 10 - Belgia
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
    imagine_url='circuite/img/Spa.png',
)
models.MarePremiu.objects.create(
    circuit=circuit10,
    nume='Marele Premiu al Belgiei',
    runda=10,
    data_cursei=date(2026, 7, 19),
)

# Runda 11 - Ungaria
circuit11 = models.Circuit.objects.create(
    nume='Hungaroring',
    tara='Ungaria',
    oras='Budapesta',
    latitudine=47.5789,
    longitudine=19.2486,
    lungime_km=4.381,
    numar_viraje=14,
    an_prima_cursa=1986,
    istorie='Este un circuit stramt si plin de viraje, unde e greu sa depasesti. De multe ori e foarte cald aici in mijlocul verii.',
    imagine_url='circuite/img/Budapesta.png',
)
models.MarePremiu.objects.create(
    circuit=circuit11,
    nume='Marele Premiu al Ungariei',
    runda=11,
    data_cursei=date(2026, 7, 26),
)

# Runda 12 - Olanda
circuit12 = models.Circuit.objects.create(
    nume='Circuit Zandvoort',
    tara='Olanda',
    oras='Zandvoort',
    latitudine=52.3888,
    longitudine=4.5409,
    lungime_km=4.259,
    numar_viraje=14,
    an_prima_cursa=1952,
    istorie='Este langa mare, printre dune de nisip din Olanda. Are viraje inclinate, ca la ovalele americane, care ajuta masinile sa treaca mai repede prin ele.',
    imagine_url='circuite/img/Zandvoort.png',
)
models.MarePremiu.objects.create(
    circuit=circuit12,
    nume='Marele Premiu al Olandei',
    runda=12,
    data_cursei=date(2026, 8, 23),
)

# Runda 13 - Italia
circuit13 = models.Circuit.objects.create(
    nume='Autodromo Nazionale Monza',
    tara='Italia',
    oras='Monza',
    latitudine=45.6156,
    longitudine=9.2811,
    lungime_km=5.793,
    numar_viraje=11,
    an_prima_cursa=1950,
    istorie='Este numit Templul Vitezei pentru ca aici se ating cele mai mari viteze din sezon. Fanii echipei Ferrari, numiti tifosi, umplu tribunele in fiecare an.',
    imagine_url='circuite/img/Monza.png',
)
models.MarePremiu.objects.create(
    circuit=circuit13,
    nume='Marele Premiu al Italiei',
    runda=13,
    data_cursei=date(2026, 9, 6),
)

# Runda 14 - Spania (Madrid), circuit nou in 2026
circuit14 = models.Circuit.objects.create(
    nume='Madring',
    tara='Spania',
    oras='Madrid',
    latitudine=40.4637,
    longitudine=-3.6167,
    lungime_km=5.474,
    numar_viraje=22,
    an_prima_cursa=2026,
    istorie='Este cel mai nou circuit din calendar si debuteaza chiar in 2026. Este un amestec de strazi si portiuni de circuit, langa targul IFEMA din Madrid.',
    imagine_url='circuite/img/Madrid.png',
)
models.MarePremiu.objects.create(
    circuit=circuit14,
    nume='Marele Premiu al Spaniei',
    runda=14,
    data_cursei=date(2026, 9, 13),
)

# Runda 15 - Azerbaidjan
circuit15 = models.Circuit.objects.create(
    nume='Baku City Circuit',
    tara='Azerbaidjan',
    oras='Baku',
    latitudine=40.3725,
    longitudine=49.8533,
    lungime_km=6.003,
    numar_viraje=20,
    an_prima_cursa=2016,
    istorie='Este un circuit de strada prin orasul vechi. Are o linie dreapta foarte lunga langa mare si o portiune ingusta pe langa un castel vechi.',
    imagine_url='circuite/img/Baku.png',
)
models.MarePremiu.objects.create(
    circuit=circuit15,
    nume='Marele Premiu al Azerbaidjanului',
    runda=15,
    data_cursei=date(2026, 9, 27),
)

# Runda 16 - Singapore
circuit16 = models.Circuit.objects.create(
    nume='Marina Bay Street Circuit',
    tara='Singapore',
    oras='Singapore',
    latitudine=1.2914,
    longitudine=103.864,
    lungime_km=4.94,
    numar_viraje=19,
    an_prima_cursa=2008,
    istorie='A fost prima cursa de formula 1 care s-a alergat noaptea, sub lumini. Se merge pe strazile orasului, iar caldura si umezeala fac cursa foarte grea pentru piloti.',
    imagine_url='circuite/img/Singapore.png',
)
models.MarePremiu.objects.create(
    circuit=circuit16,
    nume='Marele Premiu de la Singapore',
    runda=16,
    data_cursei=date(2026, 10, 11),
)

# Runda 17 - Statele Unite (Austin)
circuit17 = models.Circuit.objects.create(
    nume='Circuit of the Americas',
    tara='Statele Unite',
    oras='Austin',
    latitudine=30.1328,
    longitudine=-97.6411,
    lungime_km=5.513,
    numar_viraje=20,
    an_prima_cursa=2012,
    istorie='Are un deal abrupt chiar la primul viraj, de unde ai o priveliste peste tot circuitul. Cateva viraje sunt copiate dupa cele mai tari viraje din alte circuite din lume.',
    imagine_url='circuite/img/Austin.png',
)
models.MarePremiu.objects.create(
    circuit=circuit17,
    nume='Marele Premiu al Statelor Unite',
    runda=17,
    data_cursei=date(2026, 10, 25),
)

# Runda 18 - Mexic
circuit18 = models.Circuit.objects.create(
    nume='Autodromo Hermanos Rodriguez',
    tara='Mexic',
    oras='Ciudad de Mexico',
    latitudine=19.4042,
    longitudine=-99.0907,
    lungime_km=4.304,
    numar_viraje=17,
    an_prima_cursa=1963,
    istorie='Este asezat foarte sus fata de nivelul marii, iar aerul rarefiat face masinile sa se comporte ciudat. Are o portiune spectaculoasa care trece printr-un stadion plin de fani.',
    imagine_url='circuite/img/Mexico.png',
)
models.MarePremiu.objects.create(
    circuit=circuit18,
    nume='Marele Premiu al orasului Mexico',
    runda=18,
    data_cursei=date(2026, 11, 1),
)

# Runda 19 - Brazilia
circuit19 = models.Circuit.objects.create(
    nume='Autodromo Jose Carlos Pace (Interlagos)',
    tara='Brazilia',
    oras='Sao Paulo',
    latitudine=-23.7036,
    longitudine=-46.6997,
    lungime_km=4.309,
    numar_viraje=15,
    an_prima_cursa=1973,
    istorie='Se merge invers fata de acele ceasului si pista urca si coboara tot timpul. Aici s-au vazut unele dintre cele mai nebune curse din istorie, mai ales cand ploua.',
    imagine_url='circuite/img/SaoPaulo.png',
)
models.MarePremiu.objects.create(
    circuit=circuit19,
    nume='Marele Premiu al orasului Sao Paulo',
    runda=19,
    data_cursei=date(2026, 11, 8),
)

# Runda 20 - Statele Unite (Las Vegas)
circuit20 = models.Circuit.objects.create(
    nume='Las Vegas Strip Circuit',
    tara='Statele Unite',
    oras='Las Vegas',
    latitudine=36.1147,
    longitudine=-115.1728,
    lungime_km=6.201,
    numar_viraje=17,
    an_prima_cursa=2023,
    istorie='Se alearga noaptea chiar pe faimosul bulevard Strip, printre cazinouri si lumini. Masinile ating viteze foarte mari pe liniile drepte lungi.',
    imagine_url='circuite/img/LasVegas.png',
)
models.MarePremiu.objects.create(
    circuit=circuit20,
    nume='Marele Premiu de la Las Vegas',
    runda=20,
    data_cursei=date(2026, 11, 21),
)

# Runda 21 - Qatar
circuit21 = models.Circuit.objects.create(
    nume='Lusail International Circuit',
    tara='Qatar',
    oras='Lusail',
    latitudine=25.49,
    longitudine=51.4542,
    lungime_km=5.419,
    numar_viraje=16,
    an_prima_cursa=2021,
    istorie='Se alearga noaptea sub lumini, in desert. Este un circuit rapid, cu multe viraje lungi care ii obosesc mult pe piloti.',
    imagine_url='circuite/img/Lusail.png',
)
models.MarePremiu.objects.create(
    circuit=circuit21,
    nume='Marele Premiu al Qatarului',
    runda=21,
    data_cursei=date(2026, 11, 29),
)

# Runda 22 - Emiratele Arabe Unite (Abu Dhabi)
circuit22 = models.Circuit.objects.create(
    nume='Yas Marina Circuit',
    tara='Emiratele Arabe Unite',
    oras='Abu Dhabi',
    latitudine=24.4672,
    longitudine=54.6031,
    lungime_km=5.281,
    numar_viraje=16,
    an_prima_cursa=2009,
    istorie='De obicei aici se incheie sezonul. Cursa incepe la apus si se termina noaptea, iar circuitul trece pe langa un hotel spectaculos si un port cu iahturi.',
    imagine_url='circuite/img/AbuDhabi.png',
)
models.MarePremiu.objects.create(
    circuit=circuit22,
    nume='Marele Premiu de la Abu Dhabi',
    runda=22,
    data_cursei=date(2026, 12, 6),
)


print('Gata! Am adaugat toate cele 22 de circuite in baza de date.')
