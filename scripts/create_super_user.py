"""
python3 manage.py runscript create_super_user
"""

from django.contrib.auth.models import User
import os


def run():
    try:
        username = 'admin'
        email = 'admin@example.com'
        password = 'admin'
        if os.getenv('DA_ENVIRONMENT') == 'development':
            user = User.objects.create_superuser(username=username, email=email, password=password)

            if user is not None:
                print('Super user created!')
            else:
                print('Super user not created!')
        else:
            print('This script can only be run in development environment.')

    except Exception as err:
        print('Super user not created!', err)

