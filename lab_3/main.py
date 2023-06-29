import os
import threading

import django
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from pyngrok import ngrok

settings.configure(
    BASE_DIR=os.path.dirname("/content/PW/lab_3/"),
    DEBUG=True,
    SECRET_KEY=os.environ["DJANGO_TOKEN"],
    ALLOWED_HOSTS=["*"],
    INSTALLED_APPS=[],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": 'main.py',
        }
    },
)


django.setup()

app = get_wsgi_application()

port = 8080

public_url = ngrok.connect(port).public_url
print(f" * ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:{port}\"")

settings.BASE_URL = public_url

threading.Thread(target=app.run, kwargs={"use_reloader": False}).start()
