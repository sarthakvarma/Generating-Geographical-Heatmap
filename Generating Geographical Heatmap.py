import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

np.random.seed(42)
num_points = 200
lats = np.random.uniform(-90, 90, num_points)  
lons = np.random.uniform(-180, 180, num_points)  
data_intensity = np.random.rand(num_points)  


plt.figure(figsize=(12, 8))
m = Basemap(projection="merc", llcrnrlat=-60, urcrnrlat=85, llcrnrlon=-180, urcrnrlon=180, resolution="c")


m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color="lightblue")
m.fillcontinents(color="lightgray", lake_color="lightblue")


x, y = m(lons, lats)


scatter = m.scatter(x, y, c=data_intensity, cmap="Reds", s=50, alpha=0.8, edgecolors="k")


cb = plt.colorbar(scatter, orientation="vertical", shrink=0.5, pad=0.05)
cb.set_label("Intensity")

plt.title("Geographical Heatmap with Basemap", fontsize=16)


plt.show()
