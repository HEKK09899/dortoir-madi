from django.db import models


class DemandeDevis(models.Model):

    class Service(models.TextChoices):
        SITE_WEB = "site_web", "Site web / landing page"
        PLATEFORME = "plateforme", "Plateforme / application web"
        DESIGN = "design", "Design UI/UX et branding"
        AUTOMATISATION = "automatisation", "Automatisation"
        AUTRE = "autre", "Autre besoin"

    class Statut(models.TextChoices):
        NOUVEAU = "nouveau", "Nouveau lead"
        CONTACTE = "contacte", "Contacté"
        RDV_PLANIFIE = "rdv_planifie", "RDV planifié"
        RDV_EFFECTUE = "rdv_effectue", "RDV effectué"
        PROPOSITION_ENVOYEE = "proposition_envoyee", "Proposition envoyée"
        NEGOCIATION = "negociation", "Négociation"
        GAGNE = "gagne", "Gagné"
        PERDU = "perdu", "Perdu"

    nom = models.CharField(max_length=120)
    entreprise = models.CharField(max_length=150, blank=True)
    email = models.EmailField()
    telephone = models.CharField(max_length=30, blank=True)

    service = models.CharField(
        max_length=30,
        choices=Service.choices
    )

    budget = models.CharField(max_length=100, blank=True)
    message = models.TextField()

    statut = models.CharField(
        max_length=30,
        choices=Statut.choices,
        default=Statut.NOUVEAU
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Demande de devis"
        verbose_name_plural = "Demandes de devis"

    def __str__(self):
        return f"{self.nom} - {self.get_service_display()}"