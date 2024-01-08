from urllib.parse import quote

config_dict = {
    'HOST': 'localhost',                #Replace with server if u have
    'PORT': 3306,                       #Default port of SQL Server
    'DATABASE_NAME': 'movie_practice',  #Name of the database
    'DATABASE_USER': 'root',
    'DATABASE_PASSWORD': quote('root')
}

#Read the information
SQLALCHEMY_DATABASE_URI = 'mysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}'.format(**config_dict)

#Application
APP_PORT = 5000

#May be not necessary
DATA_PATH = ''
SECRET_KEY = 'xyz'