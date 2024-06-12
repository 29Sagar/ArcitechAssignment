# ArcitechAssignment
This is the backend repo for ArcitechAssignment app 

### Local Development
#### Prerequisites
- Python 3.10 ([Python Installation](https://www.python.org/downloads/source/))
- Pip3
- Python Virtual Environment

### Configuring the Environment
```bash
$ source env/bin/activate

#### Initial Steps

Install Requirements
```bash
$ pip install -r requirements.txt
```

Run Initial Migration
```bash
$ python manage.py migrate
```

Create a django superuser
```bash
$ python manage.py createsuperuser
```

Run Django Server
```bash
$ python manage.py runserver 8001
```

Open Html file using following path for frontend
```bash
ArcitechAssignment/templates/index.html
```
