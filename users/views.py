from rest_framework import views, status
from django.contrib.auth import authenticate
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny


# ----- Login ------
class LoginView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token, create = Token.objects.get_or_create(user=user)
            return Response({
                "message": "Login Successfully",
                'data': UserSerializer(user).data,
                "token": token.key
            })
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
