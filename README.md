# Music Junkie REST API

---

Django REST Framework for Music Junkie

---

### Launching the Music Junkie API

1. Create a new directory in your terminal of choice
1. Clone down the repository by clicking the "Clone or Download" button
1. In your terminal write: `git@github.com:evanreynolds1116/MusicJunkie-API.git`
1. `cd` into MusicJunkie-API

---

Now, set up your virtual environment:

1. `python -m venv musicenv`
1. Activate virtual environment:
    - **Mac**
      - `source ./musicenv/bin/activate`
    - **Windows** Maybe need to use Scripts
      - `source ./musicenv/Scripts/activate`
1. Install dependencies:
    - `pip install -r requirements.txt`
1. Run migrations:
    - `python manage.py migrate`
1. Create a superuser for your local version of the app:
    - `python manage.py createsuperuser`
1. Now run the server:
    - `python manage.py runserver`
. [Click here to launch the front-end](https://github.com/evanreynolds1116/MusicJunkie-FrontEnd)

---
