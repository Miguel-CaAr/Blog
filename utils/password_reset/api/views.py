from django.core.mail import send_mail
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from .serializers import PasswordResetConfirmSerializer, PasswordResetSerializer
from users.models import User
from rest_framework.exceptions import ValidationError


class PasswordResetView(APIView):
    serializer_class = PasswordResetSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']

            # Verificar si existe un usuario con ese correo
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'detail': 'No existe ningún usuario registrado con ese correo.'}, status=status.HTTP_404_NOT_FOUND)

            # Generar un token para agregar al url
            refresh_token = RefreshToken.for_user(user)
            reset_link = f'http://ejemplo.com/reset-password/{str(refresh_token.access_token)}'
            send_mail(
                'Recueperacion de contraseña',
                f'Para restablecer su contraseña, haz click en el siguiente enlace: {reset_link}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return Response({'detail': 'Email enviado con instrucciones para restablecer la contraseña.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmView(APIView):
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            
            #Obtener las pass
            new_password = serializer.validated_data['new_password']
            confirm_password = serializer.validated_data['confirm_password']

            #Validar que las pass coincidan
            if new_password != confirm_password:
              raise ValidationError({'password':'Las contraseñas no coinciden.'})
            
            #Obtener el token de los headers
            token = request.headers.get('Authorization'.split(' '))[1]
            if not token:
              raise ValidationError({'token':'Token no proporcionado o inválido.'})
            
            #Decodificar el token para obtener el usuario
            try:
              access_token = AccessToken(token)
              user_id = access_token['user_id']
              user = User.get(id=user_id)
            except Exception:
              raise ValidationError({'token':'Token no válido o expirado.'})
            
            #Cambiar contraseña
            user.set_password(new_password)
            user.save()
            
            return Response({'sucess':'Contraseña cambiada'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
              