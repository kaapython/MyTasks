KEY = 'zvf!0#5pbgvn&n40@e8uk8=vmg82_vv$$=r#run&wry6zza87c'

DEBUG = True

HOSTS = ['127.0.0.1', 'myTasks']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mytasks',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}