from .models import Cancer
from rest_framework.serializers import ModelSerializer

class CancerSerializer(ModelSerializer):
    class Meta:
        model = Cancer
        fields = '__all__'