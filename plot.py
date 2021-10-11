import matplotlib.pyplot as plt
import numpy as np

t = [ 162.5, 167.5, 172.5, 172.5, 172.5, 172.5, 172.5, 172.5, 172.5, 172.5, 172.5, 172.5, 172.5, 177.5, 177.5, 177.5, 177.5, 177.5, 177.5, 177.5, 177.5, 177.5, 177.5, 177.5, 177.5, 177.5, 182.5, 182.5, 182.5, 182.5, 182.5]
p = [ 47.5, 57.5, 52.5, 52.5, 52.5, 52.5, 57.5, 62.5, 62.5, 62.5, 67.5, 72.5, 72.5, 52.5, 57.5, 62.5, 62.5, 67.5, 67.5, 67.5, 72.5, 72.5, 72.5, 72.5, 77.5, 92.5, 67.5, 72.5, 77.5, 77.5, 97.5]

# 1D TODO
# diagramme en bâton
# diagramme boîte
# graphiques cumulatifs
# diagrammes en colonnes, en barre ou en secteurs

# histogramme
plt.hist(t, bins=[160, 165, 170, 175, 180, 185, 190])
plt.show()

# 2D TODO
# Nuage de points
# diagramme boîtes parallèles
# diagramme de profils
# diagramme en mosaïque
# juxtaposition d'histogramme