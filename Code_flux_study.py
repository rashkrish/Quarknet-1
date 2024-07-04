#Code for Correlogram

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1=pd.read_csv("C:/Users/hp/Desktop/Book1.csv",header=0,index_col=0)
print("First 5 rows datset:-\n\n",df1.head())
plt.figure(figsize=(12,10), dpi= 90)
sns.heatmap(df1.corr(), xticklabels=df1.corr().columns, yticklabels=df1.corr().columns, cmap='RdYlGn', center=0, annot=True)
plt.title('Correlogram of Flux Study Dataset', fontsize=24)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12,rotation=0)
plt.show()
