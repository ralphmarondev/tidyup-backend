from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserModel
from .serializers import UserSerializer


class UserRegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(data['password'])  # Hash password before saving
            user.save()
            return Response({
                'success': True,
                'message': 'User registered successfully',
                'user': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'message': 'Registration failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = UserModel.objects.get(username=username, is_deleted=False)
        except UserModel.DoesNotExist:
            return Response({'success': False, 'message': 'User not found or deleted'},
                            status=status.HTTP_404_NOT_FOUND)

        if user.check_password(password):
            return Response({'success': True, 'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
