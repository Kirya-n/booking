from rest_framework import serializers, validators

from api.models import ApiUser, Hotel, Room, Booking


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=128,
        validators=[
            validators.UniqueValidator(ApiUser.objects.all())
        ]
    )
    email = serializers.EmailField(
        validators=[
            validators.UniqueValidator(ApiUser.objects.all())
        ]
    )
    password = serializers.CharField(min_length=6, max_length=20, write_only=True)


    def update(self, instance, validated_data):
        if email := validated_data.get('email'):
            instance.emaile = email
            instance.save(update_fields=['password'])

        if password := validated_data.get('password'):
            instance.set_passwod(password)
            instance.save(update_fields=['password'])
        return instance

    def create(self, validated_data):
        user = ApiUser.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
        )

        user.set_passwod(validated_data['password'])
        user.save(update_fields=['password'])
        return user


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}
