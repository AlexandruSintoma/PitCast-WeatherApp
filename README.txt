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


NOTA pentru Windows / PowerShell
Daca la pasul 1 comanda "env\Scripts\activate" iti da o eroare ca scripturile
sunt blocate, ai doua variante simple:
- folosesti Command Prompt (cmd) in loc de PowerShell, unde activate merge, SAU
- nu mai activezi deloc si scrii "env\Scripts\python.exe" in loc de "python" la
  comenzile de mai sus. Exemplu: env\Scripts\python.exe manage.py runserver


CHEIA PENTRU VREME (OpenWeatherMap)
Ca sa apara vremea am nevoie de o cheie gratuita de la openweathermap.org
(imi fac cont, intru la sectiunea API keys si copiez cheia).
Cheia nu este pusa in cod, ca sa nu ajunga publica pe GitHub.
Ca sa merga vremea, creez un fisier nou numit pitcast/cheie_locala.py
si scriu in el o singura linie:
      OPENWEATHER_API_KEY = 'cheia_mea_aici'
Daca nu pun nicio cheie, site-ul merge normal, doar ca in loc de vreme scrie
"Vremea nu este disponibila momentan".


CONT DE ADMIN
utilizator: admin
parola: admin1234
