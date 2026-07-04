from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # tot ce nu e admin trimit catre aplicatia circuite
    path('', include('circuite.urls')),
]
