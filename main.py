from src.excel import leer_stats
from src.engine import calcular_pesos
n=leer_stats('data/Q2.xlsx')
r=calcular_pesos(n)
print('TOP10')
[print(x.numero,round(x.peso,5)) for x in r[:10]]
