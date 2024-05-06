import pandas as pd

xlsx_imiona = pd.ExcelFile('imiona.xlsx')
df_imiona = pd.read_excel(xlsx_imiona)
#1.1
# print(df_imiona[df_imiona['Liczba']>1000])
#1.2
# print(df_imiona[df_imiona['Imie']=='SEBASTIAN'])
#1.3
# print(df_imiona['Liczba'].sum())
#1.4
# q = df_imiona[(df_imiona.Rok >= 2000) & (df_imiona.Rok <= 2005)]
# print(q['Liczba'].sum())
#1.5
# w = df_imiona[df_imiona['Plec']=='M']
# print(w['Liczba'].sum())
# e = df_imiona[df_imiona['Plec']=='K']
# print(e['Liczba'].sum())
#1.6
# for i in range(2000, 2018):
#     rM = df_imiona[(df_imiona.Rok == i) & (df_imiona.Plec == 'M')]
#     rK = df_imiona[(df_imiona.Rok == i) & (df_imiona.Plec == 'K')]
#     rM2 = rM['Liczba'].max()
#     rK2 = rK['Liczba'].max()
#     print(rM[rM['Liczba'] == rM2])
#     print(rK[rK['Liczba'] == rK2])
#1.7
# tM = df_imiona[(df_imiona.Plec == 'M')].max()
# tK = df_imiona[(df_imiona.Plec == 'K')].max()
# print(tM)
# print(tK)

df_zamowienia = pd.read_csv('zamowienia.csv', sep=";", decimal=".")

#2.1
# print(df_zamowienia['Sprzedawca'].unique())
#2.2
# print(df_zamowienia['Utarg'].nlargest(n=5))
#2.3
