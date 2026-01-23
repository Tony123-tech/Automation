# First Machine Learning Model 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
# Settings
pd.set_option('display.max_columns', None)
plt.style.use('seaborn-v0_8')

iris = load_iris()
print("Feature names: ", iris.feature_names)
print("Target names: ", iris.target_names)
print("Datasets shape: ", iris.data.shape)

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
df['flower_name'] = df['target'].apply(lambda x: iris.target_names[x])
print(df.head())
