# Marshmallow API Prototype Docs

Last Edited: May 27, 2018 8:07 PM

Need to create an sqlite database, and add the filepath as an environmental variable to run this. Entry point for the app is the `run_app.py` script. 

1. `$ sqlite3 database.db`
2. `$ export local_db_uri=sqlite:///<full path to db file>`
  - or `$ export local_db_uri=sqlite://<relative path to db file>`
3. `$ python -m run_app`