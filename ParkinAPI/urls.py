from django.urls import path, include
from rest_framework.routers import DefaultRouter
from AppParking.views import (
    ParqueaderoView, VehicleEntryView, VehicleExitView, PasswordResetView,
    UserRegistrationView, UsuarioView, TarifaView, PropietarioView,
    PropietarioByEdad, VehiculoView, EntradaSalidaView, ParkingAvailabilityView,
    AuthTokenView, VehicleSearchView, AvailableParkingSpotsView,
    ParkingSpotDetailView, CreateParkingSpotView, UpdateParkingSpotView,
    DeleteParkingSpotView
)

router = DefaultRouter()
router.register(r'parqueaderos', ParqueaderoView)
router.register(r'usuarios', UsuarioView)
router.register(r'tarifas', TarifaView)
router.register(r'propietarios', PropietarioView)
router.register(r'vehiculos', VehiculoView)
router.register(r'entradas-salidas', EntradaSalidaView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/vehicle-entry/', VehicleEntryView.as_view(), name='vehicle-entry'),
    path('api/vehicle-exit/', VehicleExitView.as_view(), name='vehicle-exit'),
    path('api/password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/propietarios-by-edad/', PropietarioByEdad.as_view(), name='propietarios-by-edad'),
    path('api/parking-availability/', ParkingAvailabilityView.as_view(), name='parking-availability'),
    path('api/auth-token/', AuthTokenView.as_view(), name='auth-token'),
    path('api/vehicle-search/', VehicleSearchView.as_view(), name='vehicle-search'),
    path('api/available-parking-spots/', AvailableParkingSpotsView.as_view(), name='available-parking-spots'),
    path('api/parking-spot-detail/<int:pk>/', ParkingSpotDetailView.as_view(), name='parking-spot-detail'),
    path('api/create-parking-spot/', CreateParkingSpotView.as_view(), name='create-parking-spot'),
    path('api/update-parking-spot/<int:pk>/', UpdateParkingSpotView.as_view(), name='update-parking-spot'),
    path('api/delete-parking-spot/<int:pk>/', DeleteParkingSpotView.as_view(), name='delete-parking-spot'),
]