
from django.urls import path
from . import views

app_name = "vitrine"

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("nectivate/", views.nectivate, name="nectivate"),
    path("devis/", views.demande_devis, name="demande_devis"),
]
