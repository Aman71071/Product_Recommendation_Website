import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sklearn
from sklearn.decomposition import TruncatedSVD

class Engine:

    def __init__(self):

        self.amazon_ratings = pd.read_csv('ratings_Beauty.csv')
        self.amazon_ratings = self.amazon_ratings.dropna()

        self.amazon_ratings = self.amazon_ratings.head(10000)

        #Utility Matrix based on products sold and user reviews
        self.ratings_utility_matrix = self.amazon_ratings.pivot_table(values='Rating', index='UserId', columns='ProductId', fill_value=0)

        self.X = self.ratings_utility_matrix.T

        #Decomposing the Matrix
        self.SVD = TruncatedSVD(n_components=10)
        self.decomposed_matrix = self.SVD.fit_transform(self.X)

        #Correlation Matrix
        self.correlation_matrix = np.corrcoef(self.decomposed_matrix)

        self.product_names = list(self.X.index)

        self.min_confidence = 0.90

    
    def recommend(self, pid = "6117036094"):

        product_ID = self.product_names.index(pid)
        correlation_product_ID = self.correlation_matrix[product_ID]
        Recommend = list(self.X.index[correlation_product_ID > self.min_confidence])

        # Removes the item already bought by the customer
        Recommend.remove(pid) 

        return Recommend[0:9]