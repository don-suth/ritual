from get_docker_secret import get_docker_secret
from environs import Env

env = Env()
env.read_env()

# Allowed Hosts
ALLOWED_HOSTS = [
	"beta.phylactery.gozz.id.au",
]

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

# For linking Discord accounts
SOCIALACCOUNT_PROVIDERS = {
	"discord": {
		"APPS": [
			{
				"client_id": "934080121881649233",
				"secret": get_docker_secret("discord_oauth_token", safe=False),
			}
		]
	}
}
