import json
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import datasets




# Import data into python as dataframe
df1 = pd.read_csv('DataFrame.csv')
#df1 = df1.dropna()
#print(df1['Population'].dtype)
'''print(df1['Population2'].dtype)
print(df1['Land'].dtype)
print(df1['Tranpostation'].dtype)
print(df1['Age'].dtype)
print(df1['Diversity'].dtype)
print(df1['Education'].dtype)
print(df1['Eco Score'].dtype)'''

y = df1['Eco Score']
XX = df1.drop(['Eco Score'], axis=1)

#ax = sns.countplot(y, label="Count")  # M = 212, B = 357
#Eco9, Eco6, Eco2 = y.value_counts()
#print('Number of Lane Changes: ', LaneChange)
#print('Number of No lane Changes : ', NoLaneChange)

# Finding data impact on features
describe = (XX.describe())
data_dia = y
data_n = XX
data_n_2 = (XX - XX.mean())/(XX.std())  # standardization
data = pd.concat([y, data_n_2.iloc[:, 5:14]], axis=1)
data = pd.melt(data, id_vars="Eco Score",
                 var_name="features",
                 value_name='value')
data['Eco Score'] = (data['Eco Score']).astype(int)
data['value'] = data['value'].astype(float)

plt.figure(figsize=(10, 10))
sns.boxplot(x="features", y="value", hue="Eco Score", data=data)
plt.xticks(rotation=90)
plt.grid()
#plt.show()

plt.figure(figsize=(10, 10))
sns.violinplot(x="features", y="value", hue="Eco Score", data=data , inner="quart")
plt.xticks(rotation=90)
plt.grid()
#plt.show()

plt.figure(figsize=(10, 10))
sns.swarmplot(x="features", y="value", hue="Eco Score", data=data)
plt.xticks(rotation=90)
plt.grid()
#plt.show()

plt.figure()
ax = plt.subplots(figsize=(18, 18))
sns.heatmap(XX.corr(), annot=True, linewidths=.5, fmt='.1f')
plt.xticks(rotation=90)
plt.yticks(rotation=90)
#plt.show()

model = ExtraTreesClassifier()
model.fit(XX, y)
print(model.feature_importances_)
plt.figure()
plt.plot(model.feature_importances_)
yy = model.feature_importances_
plt.bar(np.array(range(13)), yy, width=0.8, bottom=None)
plt.grid()
plt.xlabel('Factors')
plt.ylabel('Relative Factor Importance')
plt.title('Which Factor is Having a High Impact on Green Score?')
plt.show()

data = pd.melt(data, id_vars="LaneChanges",
                 var_name="features",
                 value_name='value')

parsed_json = (json.loads('response_1569077064492.json'))
df = pd.read_csv('GarbageData.csv')
ax = sns.catplot(x=df['Diversity'], hue=df['Eco Score'])
plt.show()

#ax = sns.swarmplot(x='Diversity', y="Eco Footprint", data=df)
Diversityind = pd.DataFrame(df.index.tolist())
df['Diversityind'] = Diversityind
sns.catplot(x="Diversityind", y="Diversity", hue="Eco Score", kind="swarm", data=df)
plt.show()

with open("response_1569077064492.json") as json_file:
    json_data = json.load(json_file)
    print(json_data)

print('Hello')