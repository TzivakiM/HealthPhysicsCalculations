import pandas as pd
import numpy as np
import math


df = pd.read_csv("INPUTnuclide_halflives.csv",sep=",")

DecayConst = []
halflife = []

for index, row in df.iterrows():
	#print(index)
	if str(row.unit) == 's':
		halflife.append(row.Thalf)
	elif str(row.unit)=='m':
		halflife.append(row.Thalf*60)
	elif str(row.unit)=='h':
		halflife.append(row.Thalf*60*60)
	elif str(row.unit)=='d':
		halflife.append(row.Thalf*60*60*24)
	elif str(row.unit)=='y':
		halflife.append(row.Thalf*60*60*24*365)

df['halflife']=halflife

#print(type(df))
#print(df.head(1))

for thalf in df['halflife']:
	#print(thalf)
	d_const = math.log(2)/(thalf)
	#print(d_const)
	DecayConst.append(d_const)
df['DecayConst']=DecayConst

dfCompare = pd.read_csv("nuclide_decayConst_OIL.csv",sep=",")
#print(dfCompare.head(1))
df['OILDecayConst']=dfCompare['OILDecayConst']

df['comparison'] = np.where(df['OILDecayConst'] == df['OILDecayConst'] , 'true', 'false')


#print df
df.to_csv('OUTnuclides_decayConstComparison.csv')