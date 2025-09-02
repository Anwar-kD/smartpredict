import numpy as np
from sklearn.linear_model import LinearRegression

class TemperaturePredictor:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, future_steps):
        future_X = np.array(range(1, future_steps+1)).reshape(-1, 1)
        return self.model.predict(future_X)

if __name__ == "__main__":
    # Données fictives
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([20.5, 21.0, 21.2, 22.0, 22.5])
    predictor = TemperaturePredictor()
    predictor.train(X, y)
    print("Prévisions futures:", predictor.predict(3))
