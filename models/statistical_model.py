import pandas as pd
import numpy as np

class StatisticalModel:
    def __init__(self, data):
        self.data = data
        self.hot_numbers = []

    def calculate_frequencies(self):
        number_counts = self.data.value_counts()
        self.hot_numbers = number_counts.head(HOT_NUMBERS_THRESHOLD).index.tolist()

    def predict(self):
        self.calculate_frequencies()
        prediction = np.random.choice(self.hot_numbers)
        return prediction

# Usage example
if __name__ == "__main__":
    data = pd.read_csv('data/roulette_data.csv')
    model = StatisticalModel(data['number'])
    prediction = model.predict()
    print(f"Predicted number: {prediction}")
