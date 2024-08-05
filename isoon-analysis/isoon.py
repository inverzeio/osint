import pandas as pd
import geopandas
import geodatasets
import matplotlib.pyplot as plt

df = pd.read_csv("/adjust/your/path/isoon-beeline-lbs.csv")
geometry = geopandas.points_from_xy(df.X_LONGITUDE, df.Y_LATITUDE)

geo_df = geopandas.GeoDataFrame(
    df[["CODE", "REGION", "OPERATOR", "LAC", "CELL",
        "NAME", "X_LONGITUDE", "Y_LATITUDE",
        "TYPE", "ADDRESS"]], geometry=geometry)


world = geopandas.read_file(geodatasets.get_path("naturalearth.land"))

fig, ax = plt.subplots(figsize=(24, 18))
world.plot(ax=ax, alpha=0.4, color="grey")
geo_df.plot(column="ADDRESS", ax=ax, legend=True)
plt.title("IS00N Geolocations of leaked beeline-lbs.txt")
plt.show()
