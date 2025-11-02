"""Calcul de l'indice de masse corporelle (IMC / BMI).

Fonctions:
 - calculate_bmi(weight_kg, height_m) -> float
 - bmi_category(bmi) -> str (catégorie en français)

Le module fournit aussi un petit CLI pour usage interactif.
"""
from __future__ import annotations

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calcule l'IMC.

    Args:
        weight_kg: poids en kilogrammes (> 0)
        height_m: taille en mètres (> 0). Si l'utilisateur passe des cm (>= 3)
                  le CLI convertira en mètres; cette fonction exige des mètres.

    Returns:
        IMC (float) non arrondi.

    Raises:
        ValueError: si weight_kg <= 0 ou height_m <= 0
    """
    if weight_kg <= 0:
        raise ValueError("Le poids doit être un nombre strictement positif.")
    if height_m <= 0:
        raise ValueError("La taille doit être un nombre strictement positif (en mètres).")
    return weight_kg / (height_m * height_m)


def bmi_category(bmi: float) -> str:
    """Retourne la catégorie d'IMC en français suivant les seuils WHO.

    Seuils (kg/m²):
      < 18.5 : Maigreur
      18.5–24.9 : Normal
      25–29.9 : Surpoids
      30–34.9 : Obésité (classe I)
      35–39.9 : Obésité (classe II)
      >=40 : Obésité (classe III)
    """
    if bmi < 18.5:
        return "Maigreur"
    if bmi < 25:
        return "Normal"
    if bmi < 30:
        return "Surpoids"
    if bmi < 35:
        return "Obésité (classe I)"
    if bmi < 40:
        return "Obésité (classe II)"
    return "Obésité (classe III)"


def _input_float(prompt: str) -> float:
    """Lit un float depuis l'entrée standard en bouclant jusqu'à réussite."""
    while True:
        try:
            raw = input(prompt).strip()
            if raw == "":
                print("Entrée vide — réessayez.")
                continue
            value = float(raw)
            return value
        except ValueError:
            print("Valeur invalide — entrez un nombre (ex: 70 ou 1.75).")


if __name__ == "__main__":
    print("Calculateur d'IMC (BMI)")
    print("Entrez le poids en kg et la taille en mètres ou en centimètres.")
    weight = _input_float("Poids (kg) : ")
    height = _input_float("Taille (m ou cm) : ")

    # Si l'utilisateur a fourni une taille en centimètres (ex: 170),
    # on convertit: si valeur >= 3 on suppose des centimètres.
    if height >= 3:
        height = height / 100.0

    try:
        bmi_value = calculate_bmi(weight, height)
    except ValueError as exc:
        print(f"Erreur : {exc}")
    else:
        print(f"IMC : {bmi_value:.2f} kg/m²")
        print(f"Catégorie : {bmi_category(bmi_value)}")
