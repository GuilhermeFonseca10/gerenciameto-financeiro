# create_superuser.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="Guilherme").exists():
    User.objects.create_superuser("Guilherme", "guilhermeelviro2017@gmail.com", "mudar123")
    print("Superusuário criado com sucesso.")
else:
    print("Superusuário já existe.")
