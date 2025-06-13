def additionner(a, b):
    """Additionne deux nombres"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Les paramètres doivent être des nombres")
    return a + b

def est_pair(nombre):
    """Vérifie si un nombre est pair"""
    if not isinstance(nombre, int):
        raise TypeError("Le paramètre doit être un entier")
    return nombre % 2 == 0

def valider_email(email):
    """Valide un email simple (doit contenir @ et .)"""
    if "@" not in email:
        return False
    if "." not in email:
        return False
    return True

def calculer_moyenne(notes):
    """Calcule la moyenne d'une liste de notes"""
    if not isinstance(notes, list):
        raise TypeError("Le paramètre doit être une liste")
    if len(notes) == 0:
        return 0
    for note in notes:
        if not isinstance(note, (int, float)):
            raise TypeError("Toutes les notes doivent être des nombres")
    return sum(notes) / len(notes)

def convertir_temperature(celsius):
    """Convertit des degrés Celsius en Fahrenheit"""
    if not isinstance(celsius, (int, float)):
        raise TypeError("La température doit être un nombre")
    return (celsius * 9/5) + 32

def diviser(a, b):
    """Divise a par b, lève une exception si b est zéro"""
    if b == 0:
        raise ValueError("Division par zéro interdite")
    return a / b

def valider_mot_de_passe(mot_de_passe):
    """Valide un mot de passe : au moins 8 caractères"""
    return len(mot_de_passe) >= 8