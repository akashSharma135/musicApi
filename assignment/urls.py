from rest_framework.urls import path
from .views import AssignmentView

urlpatterns = [
    path('assignment/', AssignmentView.as_view())
]