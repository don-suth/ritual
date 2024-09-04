from get_docker_secret import get_docker_secret
from environs import Env

env = Env()
env.read_env()


# Django Secret Key
SECRET_KEY = get_docker_secret("django_secret_key", safe=False)

# Database
DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.postgresql",
		"NAME": env.str("POSTGRES_DB"),
		"USER": env.str("POSTGRES_USER"),
		"PASSWORD": get_docker_secret("postgres_password", safe=False),
		"HOST": env.str("DB_HOST"),
		"PORT": "5432",
	}
}

