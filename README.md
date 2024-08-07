**Flask Billboard Database Application**

This Flask application empowers you to manage a comprehensive billboard database encompassing genres, artists, and songs. Users can effortlessly submit data through intuitive forms and seamlessly view the added records via designated routes.

**Features**

- **Combined Form:** Simplifies data entry by enabling the addition of genres, artists, and songs within a single form.
- **Comprehensive View Options:** Gain a clear overview of your database with the ability to view all genres, artists, and songs independently.
- **SQLite Integration:** Leverages the robust SQLite database engine for efficient data storage and retrieval.
- **User-Friendly Interface:** Provides a clean and straightforward web interface for intuitive data manipulation.

**Prerequisites**

- Python 3.x (Download: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/))
- virtualenv ([https://virtualenv.pypa.io/en/latest/?utm_cta=retail-data-cloud-resource](https://virtualenv.pypa.io/en/latest/?utm_cta=retail-data-cloud-resource))

**Installation**

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd <repository_directory>

virtualenv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate   # Windows

2. **Create and Activate Virtual Environment:**

```bash
virtualenv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate   # Windows
```
Install Dependencies:

```bash
pip install Flask Flask-SQLAlchemy
Use code with caution.
```
3. **Run the Application:**

```bash
python app.py
```
The application will be accessible at http://127.0.0.1:5000/.

Database Setup
This application utilizes SQLite as its database engine. The database and tables will be automatically created upon the initial application run.

Application Structure
app.py: The core application file encompasses routes and models for efficient database interactions.
templates/index.html: The HTML template responsible for rendering the user interface's index page.

4. **Usage Routes**

/ (Index Page)	
GET	Renders the main page of the application.

/submit_all	POST	
Handles form submissions for adding new genres, artists, and songs.

/genres	
GET	Returns a JSON list containing all available genres.

/artists	
GET	Returns a JSON list containing all recorded artists.

/songs	
GET	Returns a JSON list containing all songs within the database.

**Example Form Submission**
To create a new genre, artist, and song, submit a form with the following fields:

Genre Name: genreName
Artist Name: artistName
Artist Country (Optional): artistCountry
Song Title: songTitle
Song Release Year: songReleaseYear
Song Duration: songDuration

5. **Virtual Environment Commands**
**Create*
```bash

virtualenv venv

**Activate* 
source venv/bin/activate  # macOS/Linux  

venv\Scripts\activate   # Windows
```
**Deactivate*
```bash

deactivate
```
License
This project is distributed under the MIT License, granting you extensive freedoms to use, modify, and distribute the code under specific terms (refer to the LICENSE file for details).