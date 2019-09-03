App is available on https://filmography.herokuapp.com/.

- `/movies/<id>`
- `/talent/<id>`
- `/graph`

I've created a visualization of a few nodes to demonstrate connectivity.  Click on a node for more information. Click to drag, double click to zoom. Two fingers on trackpad, move up or down to zoom.
The `/movies` and `/talent` endpoints are hardcoded with initial values, but can be used to query a known id (for example, Christopher Nolan, id 525, can be retrieved with `https://filmography.herokuapp.com/talent/525`, and 
The Dark Knight, id 155, can be retrieved with `https://filmography.herokuapp.com/movies/155`).   


I used data from the [Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset), movies_metadata.csv, credits.csv, ratings.csv and selected Postgresql as a database.

I created the following tables:
- crew
    - credit_id
    - department
    - film_id
    - gender
    - id
    - job
    - name
    - profile_path
- movie_cast
    - cast_id
    - character
    - credit_id
    - film_id
    - gender
    - id
    - name
    - order
    - profile_path
- genres
    - film_id
    - id
    - name
- movie_collection
    - backdrop_path
    - film_id
    - id
    - name
    - poster_path
- movies
    - adult
    - belongs_to_collection
    - budget
    - genres
    - homepage
    - id
    - imdb_id
    - original_language
    - original_title
    - overview
    - popularity
    - poster_path
    - production_companies
    - production_countries
    - release_date
    - revenue
    - runtime
    - spoken_languages
    - status
    - tagline
    - title
    - video
    - vote_average
    - vote_count
    - collection_id (refers to id in movie_collection table)
- ratings
    - userid
    - movieid
    - rating
    - timestamp
- talent
    - id
    - name
    - profile_path
  

I cleaned the data using `jupyter notebook` and `pandas`.  Cleaning consisted of using sensible null types for missing data, addressing duplicates in prospective primary key columns, etc. 
The `genres` and `movie_collection` tables were created by parsing the data from the `movies` table's `genres` and `belongs_to_collection` columns, respectively.
I used `credits.csv` to create `movie_cast` and `crew` tables, parsing the `cast` and `crew` columns respectively and adding `film_id` as a reference to `movies.id`.  Related titles
were retrieved using the `movie_collection` table and the `collection_id` column in the `movies` table.  An example of a film with a large collection: [https://filmography.herokuapp.com/movies/714](http://localhost:5000/movies/714)

I used `d3.js` for graphing and visualization.

TODO:
- tests
- clicking on node directly goes to talent or movie page -- as currently written, information about node is displayed at the top of the graph, and clicking on the name of the entity takes you to the detail page.
- full-text search, to allow querying movie or talent by name instead of by id