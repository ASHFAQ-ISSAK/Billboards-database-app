Flask Billboard Database Application
This Flask application allows users to manage a Billboard database, including genres, artists, and songs. Users can submit data via forms and view the added records through various routes.

Features
Add genres, artists, and songs through a combined form.
View all genres, artists, and songs.
Uses SQLite as the database engine.
Simple web interface for data entry.
Prerequisites
Python 3.x
virtualenv
Installation
Clone the repository:

bash
Copy code
git clone <repository_url>
cd <repository_directory>
Create and activate a virtual environment:

bash
Copy code
virtualenv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # MacOS/Linux
Install the dependencies:

bash
Copy code
pip install Flask Flask-SQLAlchemy
Run the application:

bash
Copy code
python app.py
The application will be accessible at http://127.0.0.1:5000/.

Database Setup
The application uses SQLite as the database. The database and tables will be created automatically when you run the application for the first time.

Application Structure
app.py: Main application file containing routes and models.
templates/index.html: HTML template for the index page.
Usage
Routes
Index Page:

URL: /
Method: GET
Description: Renders the index page.
Submit Combined Form:

URL: /submit_all
Method: POST
Description: Handles form submission for adding a genre, artist, and song.
View All Genres:

URL: /genres
Method: GET
Description: Returns a JSON list of all genres.
View All Artists:

URL: /artists
Method: GET
Description: Returns a JSON list of all artists.
View All Songs:

URL: /songs
Method: GET
Description: Returns a JSON list of all songs.
Example Form Submission
To add a genre, artist, and song, submit a form with the following fields:

Genre Name: genreName
Artist Name: artistName
Artist Country: artistCountry (optional)
Song Title: songTitle
Song Release Year: songReleaseYear
Song Duration: songDuration
Virtual Environment Commands
Create virtual environment:

bash
Copy code
virtualenv venv
Activate virtual environment:

bash
Copy code
venv\Scripts\activate  # Windows
# source venv/bin/activate  # MacOS/Linux
Deactivate virtual environment:

bash
Copy code
venv\Scripts\deactivate
License
This project is licensed under the MIT License.

