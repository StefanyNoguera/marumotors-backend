from rest_framework import serializers
from .models import Car, Autopart

class CarSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = '__all__'

    def get_image(self, obj):
        if obj.image:
            return obj.image.url  # ✅ full Cloudinary URL
        return None

class AutopartSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Autopart
        fields = '__all__'

    def get_image(self, obj):
        if obj.image:
            return obj.image.url  # ✅ full Cloudinary URL
        return None
