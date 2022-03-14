from rest_framework import authentication
from title.models import REview
from .serializers import REviewSerializer
from rest_framework import viewsets


class REviewViewSet(viewsets.ModelViewSet):
    serializer_class = REviewSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = REview.objects.all()
