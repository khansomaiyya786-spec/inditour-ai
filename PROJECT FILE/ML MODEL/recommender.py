import pandas as pd
from sklearn.neighbors import NearestNeighbors

class TravelRecommender:
    def __init__(self):
        self.model = NearestNeighbors(n_neighbors=5)

    def train(self, data):
        self.model.fit(data)
        print("✅ Model trained successfully!")

    def recommend(self, user_preference):
        distances, indices = self.model.kneighbors([user_preference])
        return indices