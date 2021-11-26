from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegisterView(APIView):
    def post(self, request):
        user = User.objects.create_user(username=request.data['username'],
                                 email=request.data['email'],
                                 password=request.data['password'])

        token = Token.objects.get_or_create(user=user)
        
        return Response({"token": token[0].key})


class SigninView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        token = Token.objects.get_or_create(user=user)
        
        return Response({"token": token[0].key})

