import random

movies = [
          "The Matrix",
           "The Room",
           "Titanic",
           "Shutter Island",
           "Inception",
           "Forrest Gump",
           "Green Mile",
           "Star Wars",
           "Harry Potter",
           "Batman",
           "The Lion King",
]

class DummyRecommender:

    def recommend(self):
        return "Pulp Fiction"



def get_recommendations(name, rating):
    # TODO: put your scikit model here
    if name == 'Titanic' and rating=='5':
        return ['The Beach', 'Shutter Island', 'Das Boot']
    random.shuffle(movies)
    return movies[:3]


dummy_rec = DummyRecommender()


if __name__ == "__main__":
    # this block of code is only executed when we exeute this file explicitly.
    # not when importing it
   
    # test code
    print(get_recommendations('Titanic', '5'))

    print('-'*40)

    print(get_recommendations('Star Wars', '5'))
