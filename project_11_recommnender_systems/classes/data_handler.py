import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import KNNImputer

class DataHandler:
    '''A class responsible for creating a sparse matrix from a dataframe, and imputing missing values.
    '''

    def __init__(self) -> None:
        pass


    def impute_missing_values(self):
        '''Imputes missing values on a dataframe with KNNImputer. First creates an Ratings matrix from the data.
        The data are scaled before imputing the missing values. It returns an array.
        '''
        #needs a sparse matrix
        data = self.create_sparse_matrix()

        R_= pd.DataFrame(data, index=data.index, columns=data.columns).values
        scaler = MinMaxScaler()
            
        Rscaled = scaler.fit_transform(R_)

        imputer = KNNImputer(n_neighbors=4)
        R = imputer.fit_transform(Rscaled)

        return R

    def create_sparse_matrix(self):
        '''Creates from the dataframe a sparse matrix, mostly containing 
        missing values.
        '''

        ratings = self.csv_to_df('ratings') 

        sparse_matrix = pd.pivot_table(ratings, values='rating',index='userId', columns='movieId' )

        return sparse_matrix

    def csv_to_df(self, csv_data):#rename to data
        '''takes a csv file and returns a dataframe. Takes he name of the csv as a parameter.
        '''
        #csv_name = csv_name
        #path = None
        csv_data = pd.read_csv(f'data/{0}.csv')

        return csv_data
    