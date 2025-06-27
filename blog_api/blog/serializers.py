from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'bio', 'profile_picture', 
                  'facebook', 'twitter', 'instagram', 'linkedin', 'password')
        read_only_fields = ('id',)  # Make id read-only
        extra_kwargs = { 'password': {'write_only': True} }
    
    def create(self, validated_data):
        user = get_user_model()
        newuser = user.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        newuser.set_password(validated_data['password'])
        newuser.save()
        return newuser
        