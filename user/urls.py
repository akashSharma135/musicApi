from rest_framework.urls import path

from user.views import RegisterView, SigninView

urlpatterns = [
    path('signup/', RegisterView.as_view()), 
    path('signin/', SigninView.as_view())
]