PitCast


Aplicatie web facuta in Django care arata vremea de acum la circuitele de
Formula 1 din sezonul 2026 si o mica poveste despre fiecare circuit.



CE STIE SA FACA
- Afiseaza toate circuitele din 2026 sub forma de carduri cu poza fiecarui circuit
- Are o bara de cautare dupa numele circuitului
- Pe pagina fiecarui circuit arata: date despre circuit, povestea lui, vremea de acum luata live de la un API extern, marele premiu din 2026 si comentariile lasate de vizitatori
- Vizitatorii pot lasa un comentariu printr-un formular
- Se pot adauga circuite noi printr-un formular
- Are si o pagina cu tot calendarul curselor din 2026
- Are si interfata de admin


TEHNOLOGII FOLOSITE
- Python + Django
- Bootstrap (prin CDN) pentru design
- modulul requests pentru a lua vremea de la un API extern
- API extern: OpenWeatherMap
- baza de date SQLite


BAZA DE DATE (3 tabele)
- Circuit - datele si povestea unui circuit
- MarePremiu - o cursa din 2026, legata de un circuit prin foreign key
- Comentariu - o parere lasata de un vizitator, legata de circuit prin foreign key


CUM PORNESC PROIECTUL
1. Fac mediul virtual si il activez:
      python -m venv env
      env\Scripts\activate

2. Instalez pachetele:
      pip install -r requirements.txt

3. Fac baza de date:
      python manage.py migrate

4. Bag circuitele in baza de date:
      python incarca_date.py

5. (optional) Imi fac un cont de admin:
      python manage.py createsuperuser

6. Pornesc serverul:
      python manage.py runserver

7. Deschid in browser adresa http://localhost:8000


CHEIA PENTRU VREME (OpenWeatherMap)
Ca sa apara vremea am nevoie de o cheie gratuita de la openweathermap.org
(imi fac cont, intru la sectiunea API keys si copiez cheia).
Pun cheia in fisierul pitcast/settings.py la linia:
      OPENWEATHER_API_KEY = ''
Daca las cheia goala, site-ul merge normal, doar ca in loc de vreme scrie
"Vremea nu este disponibila momentan".


CONT DE ADMIN
utilizator: admin
parola: admin1234
