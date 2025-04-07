#create a series of months between date intervals

import random
import pandas as pd
import pandas.tseries.offsets as offsets

dataincio = '2018-01-15'
datafinal = '2020-12-16'

datainciotmp = pd.to_datetime(dataincio) - offsets.MonthBegin(1)
datafinaltmp = pd.to_datetime(datafinal) + offsets.MonthEnd(0)

#cria um dataframe df com os meses entre dataincio e datafinal
df = pd.DataFrame(pd.date_range(datainciotmp, datafinaltmp, freq='MS'), columns=['data'])

#cria uma coluna com o ano
df['ano'] = df['data'].dt.year

#cria uma coluna com o mes
df['mes'] = df['data'].dt.month

#cria uma coluna com o total de dias do mes
df['dias_no_mes'] = df['data'].dt.daysinmonth

#cria uma coluna com o primeiro dia do mes
df['primeiro_dia_mes'] = df['data'] + offsets.MonthBegin(0)

#preenche a coluna primeiro_dia_mes na primeira linha do dataframe com a dataincio
df.loc[df.index[0], 'primeiro_dia_mes'] = dataincio

#cria coluna a data do ultimo dia do mes, com excepçao para a ultima linha do dataframe
df['ultimo_dia_mes'] = df['data'] + offsets.MonthEnd(0)
#preenche a coluna ultimo_dia_mes na ultima linha do dataframe com a datafinal
df.loc[df.index[-1], 'ultimo_dia_mes'] = datafinal

#cria uma coluna com o total de dias entre dataincio e datafinal
df['dias_entre_datas'] = (df['ultimo_dia_mes'] - df['primeiro_dia_mes']).dt.days + 1

#cria uma coluna com o consumo o valor é gerado aleatoriamente
df['consumo'] = random.sample(range(1, 100), len(df))

# dias_entre_datas * consumo / dias_no_mes
df['consumo_mes'] = df['dias_entre_datas'] * df['consumo'] / df['dias_no_mes']

#cria coluna com valor omip o valor é gerado aleatoriamente
df['omip'] = random.sample(range(1, 100), len(df))

#cria coluna com omip_peso = omip * consumo_mes
df['omip_peso'] = df['omip'] * df['consumo_mes']

print(df)

#media omip
omip_media = df['omip'].mean()
print('omip_media:', omip_media)

omip_ponderado = df['omip_peso'].sum() / df['consumo_mes'].sum()

print('omip_ponderado:', omip_ponderado)

