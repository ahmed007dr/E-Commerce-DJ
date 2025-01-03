# email backend to can log in with email 
#Customizing authentication in Django¶
#https://docs.djangoproject.com/en/5.1/topics/auth/customizing/  

# video 41

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class EmailOrUsernameLogin(ModelBackend):
    """
    Custom authentication backend that allows users to login using either 
    their email or username.
    """
    
    def authenticate(self, request, username=None, password=None, *args, **kwargs):
        """
        Authenticate function verifies user credentials (email/username and password)
        during login attempt.

        :param request: The incoming request
        :param username: Either email or username
        :param password: User's password
        :return: User object if credentials are valid, None otherwise
        """
        
        # First try to find user by email
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            # If user not found by email, try username
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None
        
        # Verify password if user is found
        if user.check_password(password):
            return user
        return None



#settings.py
# AUTHENTICATION_BACKENDS = [
#     'path.to.EmailOrUsernameLogin',  
        # app name . file name . class name
#     'django.contrib.auth.backends.ModelBackend', 
# ]
