import matplotlib.pyplot as plt
import numpy as np

t = [ 162.5, 167.5, 172.5, 172.5, 172.5, 172.5, 172.5, 172.5, 172.5, 172.5, 172.5, 172.5, 172.5, 177.5, 177.5, 177.5, 177.5, 177.5, 177.5, 177.5, 177.5, 177.5, 177.5, 177.5, 177.5, 177.5, 182.5, 182.5, 182.5, 182.5, 182.5]
p = [ 47.5, 57.5, 52.5, 52.5, 52.5, 52.5, 57.5, 62.5, 62.5, 62.5, 67.5, 72.5, 72.5, 52.5, 57.5, 62.5, 62.5, 67.5, 67.5, 67.5, 72.5, 72.5, 72.5, 72.5, 77.5, 92.5, 67.5, 72.5, 77.5, 77.5, 97.5]

print("-------------TAILLE--------------------------------------------------------------")
e = t
avg = np.average(e)
print(f"Moyenne: {round(avg, 4)} cm")
q2 = np.median(e)
print(f"Médiane: {q2} cm")
q1 = np.quantile(e, .25)
print(f"Premier Quartile: {q1} cm")
q3 = np.quantile(e, .75)
print(f"Troisième Quartile: {q3} cm")
print(f"Variance: {round(np.var(e), 4)}")
print(f"Ecart-type: {round(np.std(e), 4)} cm")
print("")
eu = np.unique(e)
print("Fréquence")
for ei in eu:
    occ = np.count_nonzero(e == ei)
    print(f"Taille: {ei}, Occ: {occ}, Freq: {round((occ / len(e)) * 100, 4)}%")
print("")
print(f"Etendue: {np.sort(e)[-1] - np.sort(e)[0]} cm")
print(f"Intervalle Inter-Quartile: {q3 - q1}")
ecart_absolu_moyen = 0
for ei in e:
    ecart_absolu_moyen += np.abs(avg - ei)
ecart_absolu_moyen = round(ecart_absolu_moyen / len(e), 4)
print(f"Ecart absolu moyen: {ecart_absolu_moyen}")
ecart_absolu_median = 0
for ei in e:
    ecart_absolu_median += np.abs(np.median(e) - ei)
ecart_absolu_median = round(ecart_absolu_median / len(e), 4)
print(f"Ecart absolu median: {ecart_absolu_median}")

print(f"Coefficient de variation: {round(np.std(e) / np.average(e), 4)}")
print(f"Ecart moyen relatif: {round(ecart_absolu_moyen / np.average(e), 4)}")
print(f"Coefficient Interquartile Relatif: {round((q3 - q1) / q2, 4)}")

print("-------------POIDS--------------------------------------------------------------")
e = p
avg = np.average(e)
print(f"Moyenne: {round(avg, 4)} kg")
q2 = np.median(e)
print(f"Médiane: {q2} kg")
q1 = np.quantile(e, .25)
print(f"Premier Quartile: {q1} kg")
q3 = np.quantile(e, .75)
print(f"Troisième Quartile: {q3} kg")
print(f"Variance: {round(np.var(e), 4)}")
print(f"Ecart-type: {round(np.std(e), 4)} kg")
print("")
eu = np.unique(e)
print("Fréquence")
for ei in eu:
    occ = np.count_nonzero(e == ei)
    print(f"Taille: {ei}, Occ: {occ}, Freq: {round((occ / len(e)) * 100, 4)}%")
print("")
print(f"Etendue: {np.sort(e)[-1] - np.sort(e)[0]} kg")
print(f"Intervalle Inter-Quartile: {q3 - q1}")
ecart_absolu_moyen = 0
for ei in e:
    ecart_absolu_moyen += np.abs(avg - ei)
ecart_absolu_moyen = round(ecart_absolu_moyen / len(e), 4)
print(f"Ecart absolu moyen: {ecart_absolu_moyen}")
ecart_absolu_median = 0
for ei in e:
    ecart_absolu_median += np.abs(np.median(e) - ei)
ecart_absolu_median = round(ecart_absolu_median / len(e), 4)
print(f"Ecart absolu median: {ecart_absolu_median}")

print(f"Coefficient de variation: {round(np.std(e) / np.average(e), 4)}")
print(f"Ecart moyen relatif: {round(ecart_absolu_moyen / np.average(e), 4)}")
print(f"Coefficient Interquartile Relatif: {round((q3 - q1) / q2, 4)}")