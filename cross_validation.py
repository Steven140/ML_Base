# -*- coding: utf-8 -*-
"""Cross Validation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GZImpt-FuWOYi5uyjVWMmdAzMjrVYT6w

**1. Import Libraries**
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score, KFold
from sklearn.metrics import accuracy_score

"""**2. Create Dataset**"""

np.random.seed(42)
X = np.random.rand(100, 1)
y = 2 + 3 * X + np.random.rand(100, 1)

"""**3. Create Linear Regression Model**"""

model = LinearRegression()

"""**4. Perform K-Fold Cross Validation**"""

kfold = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(model, X, y, cv=kfold, scoring='neg_mean_squared_error')
cv_scores = -cv_scores
print("Cross-Validation Scores: ")
for i, score in enumerate(cv_scores):
    print(f"Fold {i}: {score: .2f}")

"""**5. Calculate Average Cross-Validation Score**"""

avg_cv_score = np.mean(cv_scores)
print(f"Average Cross-Validation Score: {avg_cv_score: .2f}")

"""**6. Visualize**"""

import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Data Points')
X_range = np.linspace(X.min(), X.max(), 100)
y_pred = model.fit(X, y).predict(X_range.reshape(-1, 1))
plt.plot(X_range, y_pred, color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression with Cross-Validation')
plt.legend()
plt.show()