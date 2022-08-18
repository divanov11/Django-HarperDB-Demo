# HarperDB + Django Quickstart demo

A simple CRUD app using HarperDB with Django, for demo purposes. You can find a link to the full article and video [here](#)


## How to use

1 - Clone Project

```
> git clone <URL>
> cd <projectname>
> pip install -r requirements.txt
```

2 - Setup and harperDB cloud instance [here](https://harperdb.io/) and create a schema called `hackathon` and a table called `developers`. 

See video linked in artilce for details on how to do this.

2 - Connect database in `settings.py` by replacing values with your database instance.

```python
DB = harperdb.HarperDB(
    url="<your-db-url",
    username="<your-db-passsword>",
    password="<your-db-username>"
)
```

3 - start server

```
python manage.py runserver
```