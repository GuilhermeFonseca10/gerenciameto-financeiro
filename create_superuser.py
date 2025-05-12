# create_superuser.py

import os
import django

# Definir a variável de ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Checar se o superusuário já existe
if not User.objects.filter(username="admin").exists():
    # Criar superusuário
    User.objects.create_superuser("admin", "admin@example.com", "senha123")
    print("Superusuário criado com sucesso.")
else:
    print("Superusuário já existe.")
