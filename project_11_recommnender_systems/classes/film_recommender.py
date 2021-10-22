import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import KNNImputer

from sklearn.decomposition import NMF

from data_handler import DataHandler


'''
An unsupervised learning algorithm, the Non_negative Matrix Factorization (NMF) is implemented here for the movies recommendations''''


class FilmRecommender:
    '''Makes recommendations for a user, based on the NMF algorithm.
    '''

    def __init__(self):

        self.dataHandler = DataHandler()


    def get_recommendations(self, user_dict):
        '''Returns recommendations acoording to 5 movies and their ratings that the user gave as an         input'''
        
        movies = self.dataHandler.csv_to_df('movies')
        R = self.dataHandler.impute_missing_values()
        Rtrans = self.dataHandler.create_sparse_matrix()
        model, Q = self.define_model() 

        # Creates a new user and gives recommendations based on avg
        new_user = np.full(shape=(1,R.shape[1]), fill_value=Rtrans.mean().mean())

        values = user_dict.values()
        ratings = [value for key, value in enumerate(values) if key % 2 ]
        films = [value for key, value in enumerate(values) if (key % 2) == 0]
        for rating, movie in zip(ratings, films):
            new_user[0][self.title_to_id(movie)] =rating
      
        user_P = model.transform(new_user)

        actual_recommendations = np.dot(user_P, Q)
        recom_films = np.argsort(actual_recommendations)[0][:-6:-1]

        ### Translate these into movies titles from the MovieLens database
        for movie_id in recom_films:
            movies_list = movies.loc[movie_id].title
                
            return movies_list


    def get_user_input(self, name ,rating):
        '''Takes films and rating from user, creates a new user
        '''
        pass

    def title_to_id(self, title):
        '''Takes the movies titles given by the user an returns their movie_id.
        '''
        movies = self.dataHandler.csv_to_df('movies')

        return movies[movies.title==title]['movieId']


    def find_users_film_list(self, user_Id):

        movies = self.dataHandler.csv_to_df('ratings')
        watched_films = []
        films = movies.groupby(['userId']==user_Id)['movieId'].count()
        
        for film in films:
            watched_films.append(film)

        return watched_films
    
    
     def delete_watched_films(self, user_Id, user_dict):
            '''Deletes a film from the recommnedation list, if the user has already seen it'''
            
            watched_films = find_users_film_list(user_Id)
            movies_list = get_recommendations(user_dict)
            
            for film in watched_films:
                if film in movies_list:
                    movies_list.pop(film)
             
            return movies_list
            

    def define_model(self):
        '''Define and train model on the existing movie data. An unsupervised learning algorithm, the     Non_negative Matrix Factorization (NMF), is implemented here here for the recommendations
        '''
     
        data = self.dataHandler.csv_to_df('ratings')
        Rtrans = self.dataHandler.create_sparse_matrix(data)
        model = NMF(n_components=25, max_iter=500)
        fitted_model = model.fit(Rtrans)
        Q = fitted_model.components_

        return fitted_model, Q
