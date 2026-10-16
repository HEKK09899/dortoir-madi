
from django.contrib import admin
from .models import DemandeDevis


@admin.register(DemandeDevis)
class DemandeDevisAdmin(admin.ModelAdmin):

    list_display = (
        "nom",
        "entreprise",
        "email",
        "service",
        "statut",
        "created_at",
    )

    list_filter = (
        "statut",
        "service",
        "created_at",
    )

    search_fields = (
        "nom",
        "entreprise",
        "email",
        "telephone",
    )

    list_editable = ("statut",)

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    date_hierarchy = "created_at"

    ordering = ("-created_at",)
