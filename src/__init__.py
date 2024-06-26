from ucimlrepo import fetch_ucirepo
import numpy np
import pandas pd
forest_fires = fetch_ucirepo(id=162)
X = forest_fires.data.features
Y = forest_fires.data.targets
df = pd.DataFrame(data=X, columns=forest_fires.feature_names)
df['target'] = Y
print(forest_fires.metadata)

print(forest_fires.variables)

print(df.head(10))

print("Statistical Description:", df.describe())

print("Data Types:", df.dtypes)

print("Correlation:", df.corr(method='pearson'))
import matplotlib.pyplot as plt
plt.figure(figsize=(6.5, 6.5))
df['target'].hist()
plt.title('Histogram of Target Column')
plt.xlabel('Target Values')
plt.ylabel('Frequency')
plt.show()
n_cols = len(df.columns)
layout = (n_cols // 2, 2)
plt.figure(figsize=(6.5, 6.5))
df.hist(layout=layout, figsize=(6.5, 6.5))
plt.tight_layout()
plt.show()
import numpy as np
fig, ax = plt.subplots(figsize=(6.5, 6.5))
cax = ax.matshow(df.corr(), vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0, len(df.columns), 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(df.columns, rotation=45, ha='left')
ax.set_yticklabels(df.columns)
plt.show()
import matplotlib.pyplot as plt
plt.figure(figsize=(6.5, 6.5))
sns.barplot(x='month', y='target', data=df)
plt.title('Average Target by Month')
plt.xlabel('Month')
plt.ylabel('Average Target')
plt.show()