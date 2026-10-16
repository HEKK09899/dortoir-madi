from pathlib import Path
import polib

traductions = {
    "fr": {
        "DORTOIR MADI": "DORTOIR MADI",
        "Dortoir 3": "DORTOIR MADI",
        "Welcome to Dortoir 3": "Bienvenue à DORTOIR MADI",
        "Dortoir 3 — Dormitory services": "DORTOIR MADI — Services du dortoir",
        "Dortoir 3 — Laverie": "DORTOIR MADI — Laverie",
        "You are receiving this email because you requested a password reset for your account on Dortoir 3.": "Vous recevez cet e-mail car vous avez demandé la réinitialisation du mot de passe de votre compte sur DORTOIR MADI.",
        "The Dortoir 3 team": "L’équipe DORTOIR MADI",
        "Dormitory 3 — Overview": "DORTOIR MADI — Vue d’ensemble",
    },
    "ru": {
        "DORTOIR MADI": "Общежитие МАДИ",
        "Dortoir 3": "Общежитие МАДИ",
        "Welcome to Dortoir 3": "Добро пожаловать в общежитие МАДИ",
        "Dortoir 3 — Dormitory services": "Общежитие МАДИ — Услуги общежития",
        "Dortoir 3 — Laverie": "Общежитие МАДИ — Прачечная",
        "You are receiving this email because you requested a password reset for your account on Dortoir 3.": "Вы получили это письмо, потому что запросили сброс пароля для своей учётной записи в общежитии МАДИ.",
        "The Dortoir 3 team": "Команда общежития МАДИ",
        "Dormitory 3 — Overview": "Общежитие МАДИ — Обзор",
    },
    "en": {
        "DORTOIR MADI": "MADI DORMITORY",
        "Dortoir 3": "MADI DORMITORY",
        "Welcome to Dortoir 3": "Welcome to MADI DORMITORY",
        "Dortoir 3 — Dormitory services": "MADI DORMITORY — Dormitory services",
        "Dortoir 3 — Laverie": "MADI DORMITORY — Laundry",
        "You are receiving this email because you requested a password reset for your account on Dortoir 3.": "You are receiving this email because you requested a password reset for your account on MADI DORMITORY.",
        "The Dortoir 3 team": "The MADI DORMITORY team",
        "Dormitory 3 — Overview": "MADI DORMITORY — Overview",
    },
}

for langue, corrections in traductions.items():
    fichier = Path("locale") / langue / "LC_MESSAGES" / "django.po"

    if not fichier.exists():
        print(f"Fichier introuvable : {fichier}")
        continue

    catalogue = polib.pofile(str(fichier))
    nombre = 0

    for entree in catalogue:
        if entree.msgid in corrections:
            entree.msgstr = corrections[entree.msgid]
            nombre += 1

    catalogue.save()
    fichier_mo = fichier.with_suffix(".mo")
    catalogue.save_as_mofile(str(fichier_mo))

    print(
        f"{langue} : {nombre} entrées mises à jour "
        f"et compilées."
    )

print("Correction des traductions terminée.")