NOTE: The app has been taken down, but can be tested and run locally. 

- `/movies/<id>`
- `/talent/<id>`
- `/graph`

I've created a visualization of a few nodes to demonstrate connectivity.  Click on a node for more information. Click to drag, double click to zoom. With two fingers on trackpad, move up or down to zoom.
The `/movies` and `/talent` endpoints are hardcoded with initial values, but can be used to query a known id (for example, Christopher Nolan, `id=525`, can be retrieved with localhost:PORT/talent/525), and 
The Dark Knight, `id=155`, can be retrieved with localhost:PORT/movies/155). Additionally, you can navigate from film to talent and from talent to primary roles.


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
- avg_rating
    - film_id
    - rating
- talent
    - id
    - name
    - profile_path
- nodes
    - name
    - id
    - type
  

I cleaned the data using `jupyter notebook` and `pandas`.  Cleaning consisted of using sensible null types for missing data, addressing duplicates in prospective primary key columns, etc. 
The `genres` and `movie_collection` tables were created by parsing the data from the `movies` table's `genres` and `belongs_to_collection` columns, respectively.
I used `credits.csv` to create `movie_cast` and `crew` tables, parsing the `cast` and `crew` columns respectively and adding `film_id` as a reference to `movies.id`.  Related titles
were retrieved using the `movie_collection` table and the `collection_id` column in the `movies` table.  An example of a film with a large collection: (localhost:PORT/movies/714)

I used `d3.js` for graphing and visualization.

TODO:
- tests
- clicking on node directly goes to talent or movie page -- as currently written, information about node is displayed at the top of the graph, and clicking on the name of the entity takes you to the detail page.
- full-text search, to allow querying movie or talent by name instead of by id

PERFORMANCE CONSIDERATIONS
To reduce the response time to <200ms, first I would create an additional table updated periodically for the aggregate metrics by talent:  cumulative revenue, average rating across filmography.
I also typically like to have smaller view functions and move logic to a service layer for more straightforward testing.  Additionally, not currently using caching; designing a sound caching strategy would be useful.

Update: Created a table `avg_rating` with columns `film_id` and `rating`, which has improved the response time. In a real world scenario, would recompute periodically and update the table with new ratings.
