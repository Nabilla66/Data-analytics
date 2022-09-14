kmeans = KMeans(n_clusters=5)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
step_size = 0.01
file = "mall_customer.csv"
import pandas as pd
df = pd.read_csv(file)
df.head()
features = ['Annual_Income_(k$)', 'Spending_Score']
X = df[features]
plt.scatter(X['Annual_Income_(k$)'], X['Spending_Score']);
