# Demande l'utilisateur le nombre de Slushy qu'il veux acheter
quantite = int(input("Combien de Slushy veux tu acheter ? "))

# Vérifie les conditions et calcule le montant du rabais
if quantite >= 10:
    rabais = 0.25  # 25% de rabais
elif quantite >= 5:
    rabais = 0.15  # 15% de rabais
else:
    rabais = 0  # Pas de rabais

# le prix du Slushy sans rabais
prix_slushy = 2.50

# Calcul le total de la facture avec le rabais
total_sans_rabais = quantite * prix_slushy
montant_rabais = total_sans_rabais * rabais
total_avec_rabais = total_sans_rabais - montant_rabais

# Affiche le montant du rabais et le total de la facture
print("Montant du rabais : $", montant_rabais)
print("Total de la facture : $", total_avec_rabais)
