from django.urls import path
from users.views import (
    profile_view,
    edit_profile_view,
)

app_name = 'users'

urlpatterns = [
    path('<username>/',profile_view, name="view"),
    path('<username>/edit/',edit_profile_view, name="edit"),
]