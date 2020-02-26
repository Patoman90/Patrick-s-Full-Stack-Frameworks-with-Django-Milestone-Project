from django.contrib.auth.models import User
from django.db.models import Q


class CaseInsensitiveAuth:
    """
    Defined authenticate and get_user functions inside of a class called CaseInsensitiveAuth.
    """
    def authenticate(self, user_email_or_username=None, user_password=None):
        """
        Here the user is found when they provide their username/email and password.
        """
        users = User.objects.filter(Q(username__iexact=user_email_or_username) |
                                    Q(email__iexact=user_email_or_username))
        if not users:
            return None

        user = users[0]
        
        """
        User is returned if it is verified
        """
        if user.check_password(user_password):
            return user

        return None

    def get_user(self, user_id):
        """
        Use the Django authentication system to fetch a instance of a authorized user if they are registered.
        """
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
