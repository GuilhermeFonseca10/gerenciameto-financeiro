from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.urls import reverse

class UsuarioManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    TIPOS = (("ADMINISTRADOR", "Administrador"), ("COMUM", "Comum"))

    username = models.CharField("usuario", max_length=70)
    email = models.EmailField("email", unique=True, max_length=70, db_index=True)
    is_active = models.BooleanField("ativo", default=True, help_text="Se ativo o usuário tem permissão para acessar o sistema")
    is_staff = models.BooleanField("staff status", default=False, help_text="Se True, o usuário pode acessar o admin.")
    tipo = models.CharField("tipo do usuário", max_length=15, choices=TIPOS, default="COMUM")

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        ordering = ["username"]
        verbose_name = "usuário"
        verbose_name_plural = "usuários"

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username[:10].strip()

    def get_full_name(self):
        return self.username

    def get_absolute_url(self):
        return reverse("usuario_update", args=[str(self.id)])
