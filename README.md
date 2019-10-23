# Django Rest Framework Todo App

A Simple Django Rest API Todo list generator with Authentication

## Deploying on Local Development Server

Must need python>=3.7 and pipenv pre-installed. Clone the repo. Open terminal into that cloned repo. Then install dependency and activate env.

```bash
git clone https://github.com/codewithrakib/drf-todo.git
cd drf-todo
pipenv install
pipenv shell
```

Then go to the backend directory. Migrate database and syncdb. 

```bash
cd backend
python manage.py migrate --run-syncdb
```

Create some super user to test the app.
```bash
python manage.py createsuperuser
```

It will prompt for you to input user related data. Give those data as your own.
Now run,

```bash
python manage.py runserver
```
You can see a link in terminal. Open the link in a browser. You can see some URL. like ```admin/```, ```api/v1``` add this url after the base url. Like ```http://127.0.0.1:8000/admin/```. Now Discover this app.


## Contributors
* **Rakib Hasan** - *Initial work* - [codewithrakib](https://github.com/codewithrakib)


Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
