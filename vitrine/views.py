
from django.shortcuts import render
from .forms import DemandeDevisForm

def accueil(request):
    return render(request, "vitrine/accueil.html")


def nectivate(request):
    return render(request, "nectivate.html")

def demande_devis(request):
    if request.method == "POST":
        form = DemandeDevisForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "vitrine/devis_succes.html")
    else:
        form = DemandeDevisForm()

    return render(request, "vitrine/devis.html", {"form": form})

