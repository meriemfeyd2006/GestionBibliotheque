from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='library-index'),
    path('connexion/', views.connexion, name='connexion'),
    path('inscription/', views.inscription, name='inscription'),
    path('reserver/<int:livre_id>/', views.reserver_livre_view, name='library-reserver-livre'),
    path('recuperer/<int:reservation_id>/', views.recuperer_livre_view, name='library-recuperer-livre'),
    path('mes-reservations/', views.mes_reservations_view, name='library-mes-reservations'),
    path('mes-emprunts/', views.mes_emprunts_view, name='library-mes-emprunts'),
]
