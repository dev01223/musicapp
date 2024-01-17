from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [


    path('', home_view, name='home'),
    path('update_money/', update_saldo, name='update_money'),
    path('saque/', saque, name='saque'),
    path('playlists/', playlists, name="playlists"),
    path('update_data/', update_data, name="update_data")

 





    

    # Aqui estamos definindo a rota para a sua view home
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)