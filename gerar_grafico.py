import pandas as pd
import seaborn as sns

df_gasolina = pd.read_csv('gasolina.csv')
df_gasolina


grafico_gasolina = sns.lineplot(x='dia', y='venda', data=df_gasolina)
grafico_gasolina

grafico_gasolina.get_figure().savefig("grafico_gasolina.png")