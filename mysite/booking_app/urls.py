from django.urls import path,include
from rest_framework import routers
from .views import (UserProfileViewSet,CountryViewSet,ServicesViewSet,CityListViewSet,CityDetailViewSet,HotelListViewSet,HotelDetailViewSet,ImageHotelViewSet,
                    RoomViewSet,ImageRoomViewSet,ReviewViewSet,BookingHotelViewSet)

router=routers.DefaultRouter()

router.register(r'user_profile',UserProfileViewSet,basename='user_profile')
router.register(r'Country',CountryViewSet,basename='country')
router.register(r'Services',ServicesViewSet,basename='services')
router.register(r'Image_hotel',ImageHotelViewSet,basename='image_hotel')
router.register(r'Room',RoomViewSet,basename='room')
router.register(r'Image_room',ImageRoomViewSet,basename='image_room')
router.register(r'Review',ReviewViewSet,basename='review')
router.register(r'Booking_hotel',BookingHotelViewSet,basename='booking_hotel')


urlpatterns=[
    path('',include(router.urls)),
    path('hotel',HotelListViewSet.as_view(),name='hotel_list'),
    path('hotel/<int:pk>/',HotelDetailViewSet.as_view(),name='hotel_detail'),
    path('city',CityListViewSet.as_view(),name='city_list'),
    path('city/<int:pk>/',CityDetailViewSet.as_view(),name='list_detail')
]
