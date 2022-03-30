from .models import People
from rest_framework.generics import *
from .serializers import PeopleSerializers

class GetEveningGroupView(ListAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializers

class RegisterEveningView(CreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializers

class UpdateEveningView(RetrieveUpdateDestroyAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializers



