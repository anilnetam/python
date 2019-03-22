import cx_Oracle
import pandas as pd
import matplotlib.pyplot as plt
con=cx_Oracle.connect('system','Tom382523','localhost:1521/orcl')
cur=con.cursor()
cur.execute("select * from abc")
recs=cur.fetchmany()
print(recs)
cur.close()
con.close()
df=pd.DataFrame(data=recs, columns=['overno','teama','teamb'])

print(df)
print(df['teama'].mean)
print(df['teamb'].mean)
overno=list(df['overno'])
teama=list(df['teama'])
teamb=list(df['teamb'])
plt.plot(overno,teama,label='india')
plt.plot(overno,teamb,label='Aust')
plt.legend()
plt.show()
