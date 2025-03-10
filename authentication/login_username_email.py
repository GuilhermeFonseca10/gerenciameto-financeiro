from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

class LoginUsernameEmail(ModelBackend):
    def authenticate(self, request, **kwargs):
        username_or_email = kwargs.get("username")
        password = kwargs.get("password")
        UserModel = get_user_model()
        
        # Utiliza filter e first para evitar exceções desnecessárias
        user = UserModel.objects.filter(
            Q(username=username_or_email) | Q(email=username_or_email)
        ).first()
        
        if user and user.check_password(password):
            return user
        
        return None
