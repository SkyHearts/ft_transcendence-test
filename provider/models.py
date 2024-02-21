from django.db import models


from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):

    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
        print("Model.py: data:", data, "request:", request, "social:", sociallogin)
        user.username = data['user']
        return user