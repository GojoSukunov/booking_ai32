
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator,MinValueValidator

CHOSE_ROLES=(
('owner','owner'),
('client','client')
)


class USerProfile(AbstractUser):
    phone_number=PhoneNumberField(region='KG',default='+996')
    age=models.PositiveSmallIntegerField(default=0,validators=[MinValueValidator(16),MaxValueValidator(69)])
    profile_image=models.ImageField(upload_to='profile_image',null=True,blank=True)
    role=models.CharField(max_length=6,choices=CHOSE_ROLES,default='client')

    def __str__(self):
        return self.username

class Country(models.Model):
    country_name=models.CharField(max_length=32,unique=True)

    def __str__(self):
        return self.country_name


class City(models.Model):
    city_name=models.CharField(max_length=32)

    def __str__(self):
        return self.city_name

class Hotel(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    city=models.ForeignKey(City,on_delete=models.CASCADE,related_name='hotel')
    hotel_name=models.CharField(max_length=32)
    hotel_image=models.ImageField(upload_to='hotel-images/')
    description=models.TextField()
    owner=models.ForeignKey(USerProfile,on_delete=models.CASCADE)

    def get_avg_reviews(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return sum([i.stars for i in reviews]) / reviews.count()
        return 0
    def get_count_reviews(self):
        reviews=self.reviews.all()
        if reviews.exists():
            return reviews.count()
        return 0

    def __str__(self):
        return self.hotel_name

class ImageHotel(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images_hotel/')



class Services(models.Model):
    hotel=models.ManyToManyField(Hotel)
    service_icon=models.ImageField(upload_to='service_icon/')
    service_name=models.CharField(max_length=32,unique=True)

    def __str__(self):
        return self.service_name

class Room(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    room_number=models.PositiveSmallIntegerField(default=0)
    ROOM_TYPE=(
    ('Одноместный','Одноместный'),
    ('Двухместный','Двухместный'),
    ('Семейный','Семейный'),
    ('Люкс','Люкс'),
    )
    room_type=models.CharField(max_length=15,choices=ROOM_TYPE)
    ROOM_STATUS=(
    ('Свободен','Свободен'),
    ('Забронирован','Заброниован'),
    )
    room_status=models.CharField(max_length=15,choices=ROOM_STATUS)
    price=models.PositiveSmallIntegerField(default=0)


    def __str__(self):
        return f'{self.room_number}:{self.hotel}'
class ImageRoom(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images_room/')


class Review(models.Model):
    user =models.ForeignKey(USerProfile,on_delete=models.CASCADE)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='reviews')
    comment=models.TextField(null=True,blank=True)
    stars=models.PositiveSmallIntegerField(choices=[(i,str(i)) for i in range(1,10)])
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
class BookingHotel(models.Model):
    user=models.ForeignKey(USerProfile,on_delete=models.CASCADE)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    check_in=models.DateField()
    check_out=models.DateField()
    grow_up=models.PositiveSmallIntegerField(default=0)
    child=models.PositiveSmallIntegerField(default=0)
    create_date=models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.user}:{self.hotel}'