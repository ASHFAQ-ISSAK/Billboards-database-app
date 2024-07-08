from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Genre model
class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

# Define the Artist model
class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=True)

# Define the Song model
class Song(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.String(10), nullable=False)

# Route for rendering the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the combined form submission
@app.route('/submit_all', methods=['POST'])
def submit_all():
    try:
        # Insert genre
        genre_name = request.form['genreName']
        genre = Genre(name=genre_name)
        db.session.add(genre)

        # Insert artist
        artist_name = request.form['artistName']
        artist_country = request.form.get('artistCountry')
        artist = Artist(name=artist_name, country=artist_country)
        db.session.add(artist)

        # Insert song
        song_title = request.form['songTitle']
        song_release_year = request.form['songReleaseYear']
        song_duration = request.form['songDuration']
        song = Song(title=song_title, release_year=song_release_year, duration=song_duration)
        db.session.add(song)

        # Commit all changes
        db.session.commit()

        return jsonify({"message": "Data added successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to view all genres
@app.route('/genres', methods=['GET'])
def view_genres():
    genres = Genre.query.all()
    genre_list = [{"id": genre.id, "name": genre.name} for genre in genres]
    return jsonify(genre_list)

# Route to view all artists
@app.route('/artists', methods=['GET'])
def view_artists():
    artists = Artist.query.all()
    artist_list = [{"id": artist.id, "name": artist.name, "country": artist.country} for artist in artists]
    return jsonify(artist_list)

# Route to view all songs
@app.route('/songs', methods=['GET'])
def view_songs():
    songs = Song.query.all()
    song_list = [{"id": song.id, "title": song.title, "release_year": song.release_year, "duration": song.duration} for song in songs]
    return jsonify(song_list)

if __name__ == '__main__':
    with app.app_context():
        # Create SQLite database and tables
        db.create_all()
    app.run(debug=True)


# create venv    =>   virtualenv venv
#activate venv   =>   venv\Scripts\activate
#deactivate venv =>   venv\Scripts\deactivate

