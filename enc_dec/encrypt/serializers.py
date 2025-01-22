from rest_framework import serializers
from .models import UserData

class UserDataSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True, required=True, error_messages={"required": "Name is required."})
    email = serializers.EmailField(write_only=True, required=True, error_messages={"required": "Email is required."})
    address = serializers.CharField(write_only=True, required=True, error_messages={"required": "Address is required."})
    location = serializers.CharField(write_only=True, required=True, error_messages={"required": "Location is required."})
    code = serializers.CharField(read_only=True)
    encrypted_data = serializers.CharField(read_only=True)
    hashed_data = serializers.CharField(read_only=True)

    class Meta:
        model = UserData
        fields = ['name', 'email', 'address', 'location', 'code', 'encrypted_data', 'hashed_data']

    def create(self, validated_data):
        """
        Handle saving user details with encryption and hashing.
        """
        name = validated_data.pop('name')
        email = validated_data.pop('email')
        address = validated_data.pop('address')
        location = validated_data.pop('location')

        user = UserData()
        user.save_user_detail(name,email, address, location)

        return user

    def to_representation(self, instance):
        """
        Modify the response to include decrypted data if needed.
        """
        data = super().to_representation(instance)
        decrypted_details = instance.decrypt_user_details()
        data['decrypted_data'] = decrypted_details  # Show decrypted data
        return data
