from django.urls import path
from . import views

# aici tin toate adresele din aplicatie
urlpatterns = [
    path('', views.pagina_principala, name='acasa'),
    path('circuit/<int:id>', views.detalii_circuit, name='detalii'),
    path('circuit/<int:id>/comentariu', views.adauga_comentariu, name='adauga_comentariu'),
    path('adauga-circuit', views.adauga_circuit, name='adauga_circuit'),
    path('curse', views.lista_curse, name='curse'),
]
