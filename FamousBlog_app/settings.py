from pathlib import Path

# --- Базові шляхи ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Режим розробки ---
DEBUG = True
ALLOWED_HOSTS = []

# --- Секретний ключ ---
SECRET_KEY = "django-insecure-ваш_унікальний_секретний_ключ_тут"

# --- База даних ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

# --- Шаблони ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],   # пусто
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]




# --- Додатки ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local apps
    'FamousBlog_app.Advertisement_app',
    'FamousBlog_app.Articles_app',
    'FamousBlog_app.Autenfication_app',  
    'FamousBlog_app.Blog_app',
    'FamousBlog_app.Categorys_app',
    'FamousBlog_app.Image_app',
    'FamousBlog_app.Technology_app',
    'FamousBlog_app.Zal_app',
    'FamousBlog_app.Art_app',
]

# --- Мідлвари ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # обов’язково перед AuthenticationMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- URL для авторизації ---
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# --- Статичні файли ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # для продакшн збірки

# --- Медіа файли ---
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --- Автоматичний тип первинного ключа ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Головний файл urls.py ---
ROOT_URLCONF = 'FamousBlog_app.urls'





