import pandas as pd
import matplotlib.pyplot as plt
names=['Bob','Jessica','many','john','mel']
births=[968,155,77,578,973]
BabyDataSet=list(zip(names,births))
print(BabyDataSet)
df=pd.DataFrame(data=BabyDataSet, columns=['Names', 'Births'])
print(df)
df.to_csv('births1880.csv', index=False, header=False)
df=pd.read_csv('births1880.csv')
print(df)
df=pd.read_csv('births1880.csv', header=None)
print(df)
df=pd.read_csv('births1880.csv',names=['Names','Births'])
print(df)
Sorted=df.sort_values(['Births'],ascending=False)
print(Sorted)
print(Sorted.head(1))
print(df['Births'].max())
print(df['Births'].mean())
print(df['Births'].std())
plt.plot([1,2,3,4,5], list(Sorted['Births']))
plt.show()
