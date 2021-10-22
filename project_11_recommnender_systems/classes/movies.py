import numpy as np
import pandas as pd

from data_handler import csv_to_df, DataHandler


class Movies:

    def __init__(self):
        
        self.data_handler = DataHandler()


    def get_movie_list(self):
        '''Given the movies.csv file it returns a list with all the movies.
        '''
        movies_data = self.data_handler.csv_to_df('movies') 
        movies = movies_data['movieId'].tolist()

        return movies




