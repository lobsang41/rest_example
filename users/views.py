# Create your views here.
from django.contrib.auth.models import User

from rest_framework.generics import ListAPIView

class UserListAPIView(ListAPIView):
    model = User
