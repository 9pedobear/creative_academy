from .models import People
from rest_framework.serializers import ModelSerializer

class PeopleSerializers(ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'
