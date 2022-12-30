# coding: utf-8
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        UserManager)
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Usuario(AbstractBaseUser):
    # 1 campo da tupla fica no banco de dados
    # 2 campo da tupla eh mostrado para o usuario
    TIPOS = (("ADMINISTRADOR", "Administrador"), ("COMUM", "Comum"))

    USERNAME_FIELD = "username"

    username = models.CharField(_("usuario"), max_length=70)
    email = models.EmailField(_("email"), unique=True, max_length=70, db_index=True)
    is_active = models.BooleanField(
        _("ativo"),
        default=False,
        help_text="Se ativo o usuário tem permissão para acessar o sistema",
    )
    tipo = models.CharField(
        _("tipo do usuário"), max_length=15, choices=TIPOS, default="COMUM"
    )

    objects = UserManager()

    class Meta:
        ordering = ["username"]
        verbose_name = _("usuário")
        verbose_name_plural = _("usuários")

    def __unicode__(self):
        return self.username

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def get_short_name(self):
        return self.username[0:10].strip()

    def get_full_name(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.id:
            self.set_password(self.password)
        super(Usuario, self).save(*args, **kwargs)

    @property
    def is_staff(self):
        if self.tipo == "ADMINISTRADOR":
            return True
        return False

    @property
    def get_absolute_url(self):
        return reverse("usuario_update", args=[str(self.id)])


# @property
# def get_delete_url(self):
# return reverse('usuario_delete', args=[str(self.id)])
