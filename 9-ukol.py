import pandas
df = pandas.read_csv("temperature.csv")

# Vypis prvnich peti radku
print(df.head())
# Mereni v Praze
praha = df.loc[df['City'] == "Prague"]
print(praha)
# Teplota vyšší než 80
teplota = df.loc[df['AvgTemperature'] >= 80]
print(teplota)
# Teplota v Evropě vyšší než 60
teplota_e = df.loc[(df['Region'] == "Europe") & (df['AvgTemperature'] >= 60)]
print(teplota_e)
# Extremní teploty
teplota_ex = df.loc[(df['AvgTemperature'] >= 80) | (df['AvgTemperature'] <= -20)]
print(teplota_ex)
