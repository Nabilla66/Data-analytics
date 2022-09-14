import streamlit as st
import numpy as np
file = "mall_customer.csv"
import pandas as pd
df = pd.read_csv(file)
df.head()
features = ['Annual_Income_(k$)', 'Spending_Score']
X = df[features]
plt.scatter(X['Annual_Income_(k$)'], X['Spending_Score']);
