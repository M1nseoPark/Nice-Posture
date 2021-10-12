DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'park',
        'USER': 'root',
        'PASSWORD': 'alstj@99',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}