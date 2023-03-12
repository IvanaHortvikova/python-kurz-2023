# Import dat
import pandas
df = pandas.read_csv("adopce-zvirat.csv", sep=";") # separátor, místo čárky je středník
print(df)
# Výpis na pozici 34 (33 protože index od 0)
data = df[["nazev_cz", "nazev_en"]].iloc[33]
print(data)