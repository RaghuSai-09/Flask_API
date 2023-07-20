import requests
from flask import Flask, render_template,request
import os
from dotenv import load_dotenv

load_dotenv()
RAPID = os.getenv("RAPID")

app = Flask(__name__)
@app.route("/movies")
def get_all_movies():
    url = "https://online-movie-database.p.rapidapi.com/title/find"
    headers = {
        "X-RapidAPI-Key": RAPID,
        "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
    }
    querystring = {"q": "fear"}
    try:
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        movies = data['results']
        return render_template("index.html", movies=movies)
    except Exception as e:
        print("Error:", e)
        return []

@app.route("/")
def hello_world():

    return render_template('home.html')

@app.route("/movies/")
def get_movies():
    search_query = request.args.get('searchQuery')
    # print(search_query)
    if not search_query:
        return render_template("index.html")
    
    url = "https://online-movie-database.p.rapidapi.com/title/find"
    querystring = {"q": search_query}
    headers = {
        "X-RapidAPI-Key": RAPID,
        "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        movies = data['results']
        # print(movies)
        return render_template("movies.html",query=search_query, movies=movies)
    except Exception as e:
        print("Error:", e)
        return []
    
    pass

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
