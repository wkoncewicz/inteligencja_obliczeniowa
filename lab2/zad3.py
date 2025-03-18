import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("iris1.csv")

sepal_length = df.values[:,0]
sepal_width = df.values[:,1]
plt.scatter(sepal_length[0:49], sepal_width[0:49], label='Setosa', color='blue', marker='o')
plt.scatter(sepal_length[50:99], sepal_width[50:99], label='Versicolor', color='orange', marker='o')
plt.scatter(sepal_length[-50:-1], sepal_width[-50:-1], label='Setosa', color='green', marker='o')

plt.title('Original Dataset')
plt.legend()
plt.show()


scaler = StandardScaler()
sepal_length_zscore = scaler.fit_transform(sepal_length.reshape(-1, 1))
sepal_width_zscore = scaler.fit_transform(sepal_width.reshape(-1, 1))
plt.scatter(sepal_length_zscore[0:49], sepal_width_zscore[0:49], label='Setosa', color='blue', marker='o')
plt.scatter(sepal_length_zscore[50:99], sepal_width_zscore[50:99], label='Versicolor', color='orange', marker='o')
plt.scatter(sepal_length_zscore[-50:], sepal_width_zscore[-50:], label='Virginica', color='green', marker='o')
plt.title('Z-score Scaling')
plt.legend()
plt.show()

min_max_scaler = MinMaxScaler()
sepal_length_min_max = min_max_scaler.fit_transform(sepal_length.reshape(-1, 1))
sepal_width_min_max = min_max_scaler.fit_transform(sepal_width.reshape(-1, 1))

plt.scatter(sepal_length_min_max[0:49], sepal_width_min_max[0:49], label='Setosa', color='blue', marker='o')
plt.scatter(sepal_length_min_max[50:99], sepal_width_min_max[50:99], label='Versicolor', color='orange', marker='o')
plt.scatter(sepal_length_min_max[-50:], sepal_width_min_max[-50:], label='Virginica', color='green', marker='o')
plt.title('Min-Max Normalization')
plt.legend()
plt.show()


# z pomocą chata, prompt:
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("iris1.csv")

# sepal_length = df.values[:,0]
# sepal_width = df.values[:,1]
# plt.scatter(sepal_length[0:49], sepal_width[0:49], label='Setosa', color='blue', marker='o')
# plt.scatter(sepal_length[50:99], sepal_width[50:99], label='Versicolor', color='orange', marker='o')
# plt.scatter(sepal_length[-50:-1], sepal_width[-50:-1], label='Setosa', color='green', marker='o')

# plt.title('Original Dataset')
# plt.legend()
# plt.show()

# can you create plot for sepal width and length with min-max normalization and with z-score scaling?