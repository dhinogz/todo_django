# Django Boilerplate

Simple Django boilerplate from William Vincent's [Django for Professionals](https://djangoforprofessionals.com/). 

Includes:
- Docker 
- PostgreSQL 14
- Built in user management with allauth
- Custom User Model set up
- Finished tests for accounts and pages app
- Pages app includes Home and About
- Base template with simple navbar and home/about templates
- Custom allauth templates
- Responsive CSS styling with Bootstrap 4
- Crispy Forms

## Installation

### Initial
First, clone repo
```bash
$ git clone https://github.com/dhinogz/django-boilerplate.git
```

Change name and change directory
```bash
$ mv django-boilerplate project_name && cd project_name
```
### Environment variables
We're gonna want to create a .env.dev file to store our environment variables
```bash
$ touch .env.dev
```

We're gonna need to generate a SECRET_KEY to paste into our .env.dev file. To do so, run following code on the command line.
```bash
$ python -c "import secrets; print(secrets.token_urlsafe())"
```
Example output:
```
2x$e%!k_u_0*gq0s4!_u(2(^lpy&gir0hg)q&5nurj0-sseuav
```
> Note: if your SECRET_KEY includes a dollar sign, $, then you need to add an additional dollar sign, $$. This is due to how docker-compose handles variable substitution. Otherwise you will see an error!

Add following text to .env.dev file:
```
DEBUG=1
SECRET_KEY= OUR GENERATED SECRET KEY
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
```

### Docker
Make sure you have Docker and docker-compose installed to build project container.
Also make sure you have pipenv installed globally to make our virtual environment in the container.

Then, type this into the command line to build and run container in detached mode. 
```bash
$ docker-compose up -d --build
```
Visit page at http://127.0.0.1:8000/
Access admin site at http://127.0.0.1:8000/admin 

After first install, make migrations and migrate
```bash
$ docker-compose exec web python manage.py makemigrations accounts
$ docker-compose exec web python manage.py migrate
```

Shut down container and build again
```bash
$ docker-compose down
$ docker-compose up -d --build
```

## Usage

### Running commands
In order to use the command line on docker, use this code snippet at the start of every command
```bash
$ docker-compose exec web
```

For example, let's suppose we want to start an app in our Docker instance. We would run the following code:
```bash
$ docker-compose exec web python manage.py startapp app_name
```

### Create super user
```bash
$ docker-compose exec web python manage.py createsuperuser
```

### Seeing logs
To display log output from our container, run following code:
```bash
$ docker-compose logs
```
This is very useful for debugging.

### Static files in production
Before deploying, we need to run collectstatic to create a single, production-ready directory of all the static files in our project.
```bash
$ docker-compose exec web python manage.py collectstatic
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)