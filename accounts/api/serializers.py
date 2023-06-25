from accounts.models import Account, AccountStatus
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    photo = serializers.ImageField(read_only=True)

    class Meta:
        model = Account
        fields = '__all__'

class AccountPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['photo']

class AccountStatusSerializer(serializers.ModelSerializer):
    user_account = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = AccountStatus
        fields = '__all__'