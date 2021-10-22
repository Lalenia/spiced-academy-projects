from flask import Flask, render_template, request, jsonify
from film_recommender import get_recommendations, FilmRecommender
from movies import Movies


app = Flask(__name__)


@app.route('/')
def index():
    movie = Movies()
    movies = movie.get_movie_list()
    return render_template('index.html', movienames=movies)


@app.route('/recommender')
def recommender():
    users_input = dict(request.args)


    top5 = get_recommendations(users_input)#takes a User instance or a dict
 
    return render_template('recommendation.html', movies=top5, title='Recommendations based on NMF')


if __name__ == "__main__":
 
    app.run(debug=True, port=5000)