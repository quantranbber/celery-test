from rest_framework import serializers

from store.models import *


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'store_id', 'name')


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogData
        fields = ('id', 'time', 'content', 'store_id', 'user_id')
