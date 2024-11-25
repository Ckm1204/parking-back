from inspect import stack
from rest_framework import generics
from AppParking.serializers import UserRegistrationSerializer
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import generics
from AppParking.models import Vehiculo
from AppParking.serializers import VehiculoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from AppParking.serializers import *

# Create your views here.

# In `AppParking/views.py`
from rest_framework import filters

class ParqueaderoView(viewsets.ModelViewSet):
    queryset = Parqueadero.objects.all()
    serializer_class = ParqueaderoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'direccion']
    ordering_fields = ['nombre', 'created_at']

class VehicleEntryView(APIView):
    def post(self, request):
        data = request.data
        vehiculo = Vehiculo.objects.get(id=data['vehiculo_id'])
        tarifa = Tarifa.objects.get(id=data['tarifa_id'])
        entrada_salida = EntradaSalida.objects.create(
            vehiculo=vehiculo,
            tarifa=tarifa,
            usuario=request.user,
            tipo='entrada'
        )
        return Response({"message": "Vehicle entry logged."}, status=status.HTTP_201_CREATED)

class VehicleExitView(APIView):
    def post(self, request):
        data = request.data
        vehiculo = Vehiculo.objects.get(id=data['vehiculo_id'])
        tarifa = Tarifa.objects.get(id=data['tarifa_id'])
        entrada_salida = EntradaSalida.objects.create(
            vehiculo=vehiculo,
            tarifa=tarifa,
            usuario=request.user,
            tipo='salida'
        )
        return Response({"message": "Vehicle exit logged."}, status=status.HTTP_201_CREATED)
class PasswordResetView(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = Usuario.objects.get(email=email)
            # Logic to send password reset email
            return Response({"message": "Password reset email sent."}, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({"error": "User with this email does not exist."}, status=status.HTTP_400_BAD_REQUEST)
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
class UsuarioView (viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
class TarifaView (viewsets.ModelViewSet):
    queryset = Tarifa.objects.all()
    serializer_class = TarifaSerializer
class PropietarioView(viewsets.ModelViewSet):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer

    def get_queryset(self):
        an = self.request.query_params.get('an')
        edad = 2024 - int(an)
        queryset = Propietario.objects.filter(edad__gte=edad)
        return queryset
class PropietarioByEdad(APIView):
    def post(self,request):
        try:
            data = request.data
            res = Propietario.objects.filter(edad__gte=int(data['edad']))
            respuesta = PropietarioSerializer(res,many=True)
            return Response(respuesta.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"mensaje":"Ocurrio un problema!!"+str(e)}, status=status.HTTP_502_BAD_GATEWAY)

class VehiculoView (viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
class EntradaSalidaView (viewsets.ModelViewSet):
    queryset = EntradaSalida.objects.all()
    serializer_class = EntradaSalidaSerializer

class ParkingAvailabilityView(APIView):
    def get(self, request):
        available_spots = Parqueadero.objects.filter(available=True).count()
        return Response({"available_spots": available_spots}, status=status.HTTP_200_OK)
class AuthTokenView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data =request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class VehicleSearchView(generics.ListAPIView):
    serializer_class = VehiculoSerializer

    def get_queryset(self):
        plate = self.request.query_params.get('plate')
        return Vehiculo.objects.filter(placa__icontains=plate)

class AvailableParkingSpotsView(generics.ListAPIView):
    serializer_class = ParqueaderoSerializer

    def get_queryset(self):
        return Parqueadero.objects.filter(available=True)

class ParkingSpotDetailView(generics.RetrieveAPIView):
    queryset = Parqueadero.objects.all()
    serializer_class = ParqueaderoSerializer

class CreateParkingSpotView(generics.CreateAPIView):
    serializer_class = ParqueaderoSerializer

class UpdateParkingSpotView(generics.UpdateAPIView):
    queryset = Parqueadero.objects.all()
    serializer_class = ParqueaderoSerializer

class DeleteParkingSpotView(generics.DestroyAPIView):
    queryset = Parqueadero.objects.all()
    serializer_class = ParqueaderoSerializer