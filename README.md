# Portafolio API

API Rest for a web portfolio. Control projects and tags. Use the Django admin site for creation and editing. Includes CORS support, Procfile (Heroku deploy) and Whitenoise for static files.

## Quickstart

First of all, clone this repo.

```
git clone https://github.com/DD21S/portfolio-api.git
```

Then, in the project directory, you install the requirements.

```
pip install -r requirements.txt
```

Set environment variables.

```
export SECRET_KEY=your_secret_key
export DEBUG=True
```

Now, make the migrations.

```
python manage.py migrate
```

Create a superuser.

```
python manage.py createsuperuser
```

And finally, run the project.

```
python manage.py runserver
```

Ready, now your API is running :&#41;

---

It's recommended to use a virtual enviroment to run Python web applications.

Create and activate one with these commands:

```
python3 -m venv venv
source ven/bin/activate
```