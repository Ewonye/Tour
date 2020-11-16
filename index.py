
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

user = User.objects.create_user('', '@.com', '')
user.last_name = ''
u = User.objects.get(username='')
u.set_password('new password')
 user.save()
user = authenticate(username='', password='')
if user is not None:
     # A backend authenticated the credentials
else:
    # No backend authenticated the credentials