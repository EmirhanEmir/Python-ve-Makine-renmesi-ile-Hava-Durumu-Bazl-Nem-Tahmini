import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Veri setini yükleyin
data = pd.read_csv("odev_tenis.csv")

# Gerekli kütüphaneler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

# Verileri etiketleyerek sayısal hale getirin
data_encoded = data.apply(LabelEncoder().fit_transform)

# 'outlook' sütununa OneHotEncoder uygulayın
outlook = data_encoded.iloc[:, :1]
ohe = OneHotEncoder()
outlook_encoded = ohe.fit_transform(outlook).toarray()

# Encode edilmiş 'outlook' verisini diğer sütunlarla birleştirin
outlook_df = pd.DataFrame(data=outlook_encoded, index=range(14), columns=["overcast", "rainy", "sunny"])
merged_data = pd.concat([outlook_df, data.iloc[:, 1:3]], axis=1)
merged_data = merged_data.iloc[:, 0:4]
merged_data = pd.concat([data_encoded.iloc[:, -2:], merged_data], axis=1)

# Bağımlı değişken olan 'humidity' sütununu ayırın
humidity = data.iloc[:, 2].values

# Veriyi eğitim ve test setlerine ayırın
X_train, X_test, y_train, y_test = train_test_split(merged_data, humidity, test_size=0.33, random_state=0)

# Lineer regresyon modelini eğitin
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Tahmin yapın
y_pred = regressor.predict(X_test)

# OLS kullanarak modeli değerlendirin
X_ols = np.append(arr=np.ones((14, 1)).astype(int), values=merged_data.iloc[:, :], axis=1)
X_values = merged_data.iloc[:, [0, 1, 2, 3, 4, 5]].values
X_values = np.array(X_values, dtype=float)

# statsmodels ile OLS regresyon modeli oluşturun ve özetini yazdırın
ols_model = sm.OLS(humidity, X_values).fit()
print(ols_model.summary())

# Belirli sütunları hariç tutarak modeli tekrar değerlendirin
merged_data_reduced = merged_data.iloc[:, 1:]
X_ols_reduced = np.append(arr=np.ones((14, 1)).astype(int), values=merged_data_reduced.iloc[:, :], axis=1)

X_values_reduced = merged_data_reduced.iloc[:, [0, 1, 2, 3, 4]].values
X_values_reduced = np.array(X_values_reduced, dtype=float)

ols_model_reduced = sm.OLS(humidity, X_values_reduced).fit()
print(ols_model_reduced.summary())

# Azaltılmış veri seti ile eğitim ve test setlerine ayırın
X_train_reduced, X_test_reduced, y_train_reduced, y_test_reduced = train_test_split(merged_data_reduced.iloc[:, 1:], humidity, test_size=0.33, random_state=0)

# Modeli yeniden eğitin ve tahmin yapın
regressor.fit(X_train_reduced, y_train_reduced)
y_pred_reduced = regressor.predict(X_test_reduced)
