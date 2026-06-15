from rest_framework import serializers
from .models import (USerProfile,Country,
        City,Services,Hotel,ImageHotel,Room,ImageRoom,Review,BookingHotel)


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model=USerProfile
        fields=['id','username']
class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields='__all__'
class CityListSerializers(serializers.ModelSerializer):
    class Meta:
        model=City
        fields=['id','city_name']
class HotelSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model=Hotel
        fields=['id','hotel_name']

class ReviewSerializers(serializers.ModelSerializer):
    user=UserProfileSerializers()
    hotel=HotelSimpleSerializers()
    class Meta:
        model=Review
        fields=['id','comment','stars','created_date','user','hotel']

class HotelDetailSerializers(serializers.ModelSerializer):
    owner=UserProfileSerializers()
    country=CountrySerializers()
    city=CityListSerializers()
    reviews=ReviewSerializers(read_only=True,many=True)
    get_avg_reviews = serializers.SerializerMethodField()
    get_count_reviews = serializers.SerializerMethodField()
    class Meta:
        model=Hotel
        fields=['country','city','owner','hotel_name','hotel_image','description','reviews',
                'get_avg_reviews','get_count_reviews']

    def get_avg_reviews(self, obj):
        return obj.get_avg_reviews()

    def get_count_reviews(self, obj):
        return obj.get_count_reviews()


class HotelListSerializers(serializers.ModelSerializer):
    country=CountrySerializers()
    city=CityListSerializers()
    class Meta:
        model=Hotel
        fields=['id','country','city','hotel_name','hotel_image']

class CityDetailSerializers(serializers.ModelSerializer):
    hotel=HotelListSerializers(many=True)
    class Meta:
        model=City
        fields=['id','city_name','hotel']

class ServicesSerializers(serializers.ModelSerializer):
    hotel=HotelSimpleSerializers(many=True)
    class Meta:
        model=Services
        fields=['id','service_icon','service_name','hotel']



class ImageHotelSerializers(serializers.ModelSerializer):
    class Meta:
        model=ImageHotel
        fields='__all__'
class RoomSerializers(serializers.ModelSerializer):
    hotel=HotelSimpleSerializers()
    class Meta:
        model=Room
        fields=['id','room_number','room_type','room_status','price','hotel']
class ImageRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model=ImageRoom
        fields='__all__'

class BookingHotelSerializers(serializers.ModelSerializer):
    user=UserProfileSerializers()
    hotel=HotelSimpleSerializers()
    room=RoomSerializers()
    class Meta:
        model=BookingHotel
        fields=['id','check_in','check_out','grow_up','child','create_date','user','hotel','room']