from rest_framework.serializers import ModelSerializer
from .models import Data

class DataSerializer(ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'
