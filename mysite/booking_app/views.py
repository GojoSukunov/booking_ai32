from rest_framework import viewsets,generics
from .models import (USerProfile,Country,
        City,Services,Hotel,ImageHotel,Room,ImageRoom,Review,BookingHotel)
from .serializers import (UserProfileSerializers,CountrySerializers,CityListSerializers,CityDetailSerializers,ServicesSerializers,HotelListSerializers,HotelDetailSerializers,ImageHotelSerializers,
    RoomSerializers,ImageRoomSerializers,ReviewSerializers,BookingHotelSerializers)
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import HotelFilter
from .pagination import HotelPagination
from rest_framework import permissions
from .permissions import CheckHotel

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset =USerProfile.objects.all()
    serializer_class = UserProfileSerializers
    permission_classes =[permissions.IsAuthenticatedOrReadOnly]
class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers
    filter_backends = [SearchFilter]
    search_fields=['service_name']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers
    filter_backends = [SearchFilter]
    search_fields=['country_name']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class CityListViewSet(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializers
    filter_backends = [SearchFilter]
    search_fields=['city_name']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = HotelPagination

class CityDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class HotelListViewSet(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializers
    filter_backends = [SearchFilter,DjangoFilterBackend]
    search_fields=['hotel_name','owner']
    filterset_class=HotelFilter
    pagination_class = HotelPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class HotelDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializers
    permission_classes = [CheckHotel]

class ImageHotelViewSet(viewsets.ModelViewSet):
    queryset = ImageHotel.objects.all()
    serializer_class = ImageHotelSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class ImageRoomViewSet(viewsets.ModelViewSet):
    queryset =ImageRoom.objects.all()
    serializer_class =ImageRoomSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class BookingHotelViewSet(viewsets.ModelViewSet):
    queryset = BookingHotel.objects.all()
    serializer_class = BookingHotelSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]